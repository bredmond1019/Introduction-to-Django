from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

from . import forms


class SignUp(CreateView):
    # This is just creating a shorter variable name for the class UserCreateForm
    # We are NOT calling an instance of the class here
    form_class = forms.UserCreateForm
    # On successful signup we will send them back to the login page
    success_url = reverse_lazy('login')
    template_name = 'accoutns/signup.html'
