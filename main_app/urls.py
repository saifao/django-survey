from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('surveys/', views.surveys_index, name='index'),
    path('surveys/create', views.surveys_create.as_view(), name='create'),
    path('survey/<int:survey_id>/questions/create', views.questions_create.as_view(), name='question_create')
]