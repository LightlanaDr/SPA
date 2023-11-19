from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('rooms/', views.rooms, name='rooms'),
    path('new2024/', views.new2024, name='new2024')
]