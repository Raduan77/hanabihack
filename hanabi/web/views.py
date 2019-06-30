from django.shortcuts import render, get_object_or_404
import json
import operator
import random

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers, parser


class LoginView(CreateAPIView):
    serializer_class = serializers.MemberSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        member, created = models.Member.objects.get_or_create(
            name=request.data["name"], user=request.user
        )
        if created:
            langs = parser.Forkwell_parser(request.data["name"]).get_user_info()
            for lang in langs.keys():
                l = models.Language.objects.get(name=lang, skill=langs[lang])
                member.languages.add(l)
                r = models.Rank.objects.create(language=l, user=member)
        return Response(
            {"name": member.name, "pk": member.pk},
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


class LanguageListAPIView(ListAPIView):
    serializer_class = serializers.LanguageSerializer

    def get_queryset(self):
        member = get_object_or_404(models.Member, user=self.request.user)
        return member.languages


class LeaderBoardAPIView(APIView):
    def get(self, request, pk):
        language = get_object_or_404(models.Language, pk=pk)
        own = language.owners.all()
        json = {}
        for member in own:
            json[member.name] = get_object_or_404(
                models.Rank, language=language, user=member
            ).amount
        sorted_json = sorted(json.items(), key=operator.itemgetter(1), reverse=True)
        return Response(sorted_json, status=status.HTTP_200_OK)


class CheckSessionAPIView(APIView):
    def get(self, request, pk):
        session = get_object_or_404(models.Session, pk=pk)
        return Response({"status": session.is_closed()})


class GetOrCreateSessionAPIView(APIView):
    def post(self, request, pk):
        language = get_object_or_404(models.Language, pk=pk)
        member = get_object_or_404(models.Member, user=request.user)
        sessions = list(
            filter(
                lambda x: not x.is_closed(),
                models.Session.objects.filter(language=language).all(),
            )
        )
        if len(sessions) == 0:
            session = models.Session.objects.create(language=language)
            session.participants.add(member)
            session.connected[member.pk] = True
            for exercise in models.Exercise.objects.all():
                exercise.session = session
            return Response({"pk": session.pk}, status=status.HTTP_201_CREATED)
        else:
            session = models.Session.objects.filter(language=language).all()[0]
            session.participants.add(member)
            session.connected[member.pk] = True
            return Response({"pk": session.pk}, status=status.HTTP_202_ACCEPTED)


class TakeResultAPIView(APIView):
    def post(self, request, pk):
        member = get_object_or_404(models.Member, user=request.user)
        session = get_object_or_404(models.Session, pk=pk)
        language = session.language
        session.finished = True
        rank = models.Rank.objects.get(language=language, user=member)
        rank.amount += random.randint(-30, 30)
        return Response(status.HTTP_200_OK)


class GetTestAPIView(APIView):
    def get(self, request):
        return Response(json.load(open("web/questions/questions.json")))

