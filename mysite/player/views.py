from django.http import HttpResponse
from django.shortcuts import render
from .models import Player
# Create your views here.


def get_player(request):
    players = Player.objects.all()

    context = {
        'players': players
    }
    return render(request, 'player/list_players.html', context )