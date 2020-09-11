from django.urls import path, include
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app' # This needs to match the href tag name

urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name = 'other')
]