from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)


class Language(models.Model):
    owners = models.ManyToManyField(Member, related_name="languages", blank=True)

    skill = models.IntegerField(default=1)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}({self.skill})"


class Rank(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    


class Session(models.Model):
    participants = models.ManyToManyField(Member, related_name="sessions")
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="sessions"
    )
    connected = JSONField(blank=True)

    result = JSONField(blank=True)


class Exercise(models.Model):
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="exercises"
    )

    text = models.TextField()
    answers = JSONField()
    creator = models.CharField(max_length=30)
    result = models.IntegerField(default=0)
