from django.urls import path, include
from users_app import views


urlpatterns = [
    path('', views.users, name = 'users'),
]