from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200)
    option_one_votes = models.IntegerField(default=0)
    option_two_votes = models.IntegerField(default=0)
    option_three_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    survey_taken = models.ManyToManyField(Survey)

