from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg
from django.shortcuts import render
from .models import Player
from .models import PlayerRate
from .forms import PlayerRateForm
from django.shortcuts import redirect
import json
# Create your views here.


def get_player(request):
    players = Player.objects.all().order_by('name')
    context = {
        'players': players,
    }
    if request.method == 'POST':
        try:
            check_rate = PlayerRate.objects.get(user=request.user, player=Player.objects.get(name=request.POST['name']))
            check_rate.rate = request.POST['rate']
            check_rate.save()
            average_rate = float(vars(Player.objects.annotate(Avg('playerrate__rate')).filter(name=request.POST['name'])[0])['playerrate__rate__avg'])
            dictionary = {'average': average_rate}
            dictionary = json.dumps(dictionary)
            print(dictionary)
            return HttpResponse(dictionary, content_type="application/json")
        except ObjectDoesNotExist:
            check_rate.rate = request.POST['rate']
            check_rate.save()

    #if request.method == 'GET':
        #print("GET")


    if request.user.is_authenticated:
        user_rate = PlayerRate.objects.filter(user=request.user).order_by('player__name')
        context['user_rate'] = user_rate
        user_rate = {x.player.name:int(x.rate) for x in user_rate }
        user_rate = json.dumps(user_rate, indent=4)
        user_rate = json.loads(user_rate)
        context['user_rate'] = user_rate

    else:
        print("no one")


    return render(request, 'player/list_players.html', context)


def add_rate(request):

    if request.method == 'POST':
        form = PlayerRateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print(form)
            print(post)
            return redirect('players')
    else:
        form = PlayerRateForm()

    context = {
        'form': form,
    }

    return render(request, 'player/add_rate.html', context )


