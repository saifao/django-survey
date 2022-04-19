from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Survey(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_owner')
    users_taken = models.ManyToManyField(User, related_name='user_taken')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('question_create', kwargs={'survey_id': self.id})

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
    
    def get_absolute_url(self):
       return reverse('question_create', kwargs={'survey_id': self.survey.id})
       ##return reverse('detail', kwargs={'survey_id': self.survey.id})

