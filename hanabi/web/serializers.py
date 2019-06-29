from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from . import models


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ("name",)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ("name", "skill")