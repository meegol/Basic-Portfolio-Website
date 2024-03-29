# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Make sure 'about' is defined
    path('contact/', views.contact, name='contact'),
    path('languages/', views.languages, name='languages'),
    path('projects/', views.projects, name='projects'),
]