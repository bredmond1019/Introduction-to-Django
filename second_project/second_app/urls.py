from django.urls import path, include
from second_app import views

urlpatterns = [
    path('', views.help, name='help')
]