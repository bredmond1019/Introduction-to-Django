from django.shortcuts import render
from django.http import HttpResponse
from second_project.second_app.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict = {'insert_me': "Help Page"}
    return render(request, 'second_app/help.html', context = my_dict)