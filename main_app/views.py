from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Survey, Question
from django.views.generic.edit import CreateView, DeleteView

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('login')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def surveys_index(request):
  surveys = Survey.objects.all()
  return render(request, 'surveys/index.html', {'surveys' : surveys})

class surveys_create(CreateView):
  model = Survey
  fields = ['name']
  success_url = '/surveys/'

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

class questions_create(CreateView):
  model = Question
  fields = ['question_text', 'option_one', 'option_two', 'option_three']

  def form_valid(self, form):
    print(self.kwargs['survey_id'])
    form.instance.survey = Survey.objects.get(id=self.kwargs['survey_id'])
    return super().form_valid(form)

def survey_detail(request, survey_id):
  print(survey_id)
  survey = Survey.objects.get(id=survey_id)
  questions = Question.objects.filter(survey=survey_id)
  return render(request, 'surveys/detail.html', {'survey': survey, 'questions': questions})