from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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
        return Response(
            {"name": member.name},
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

