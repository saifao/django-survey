from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
