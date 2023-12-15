# counter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment_button/', views.increment_button, name='increment_button'),
]
