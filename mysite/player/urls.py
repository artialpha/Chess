from django.urls import path

from . import views

urlpatterns = [
    path('players', views.get_player, name='players'),
]