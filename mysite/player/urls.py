from django.urls import path

from . import views

urlpatterns = [
    path('players', views.get_player, name='players'),
    path('rate', views.add_rate, name='rate'),
    #path(r'^search/$', views.search),
]