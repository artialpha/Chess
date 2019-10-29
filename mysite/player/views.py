from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg
from django.shortcuts import render
from .models import Player
from .models import PlayerRate
from .forms import PlayerRateForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
@login_required
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
            dictionary = {'average': average_rate, 'logged': request.user.is_authenticated}
            dictionary = json.dumps(dictionary)
            return HttpResponse(dictionary, content_type="application/json")
        except ObjectDoesNotExist:
            PlayerRate.objects.create(
                rate=request.POST['rate'],
                player=Player.objects.get(name=request.POST['name']),
                user=request.user,
            )

            average_rate = float(vars(Player.objects.annotate(Avg('playerrate__rate')).filter(name=request.POST['name'])[0])['playerrate__rate__avg'])
            dictionary = {'average': average_rate, 'logged': request.user.is_authenticated}
            dictionary = json.dumps(dictionary)
            return HttpResponse(dictionary, content_type="application/json")

    user_rate = PlayerRate.objects.filter(user=request.user).order_by('player__name')
    context['user_rate'] = user_rate
    user_rate = {x.player.name:int(x.rate) for x in user_rate }
    user_rate = json.dumps(user_rate, indent=4)
    user_rate = json.loads(user_rate)
    context['user_rate'] = user_rate

    return render(request, 'player/list_players.html', context)


def add_rate(request):

    if request.method == 'POST':
        form = PlayerRateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('players')
    else:
        form = PlayerRateForm()

    context = {
        'form': form,
    }

    return render(request, 'player/add_rate.html', context )


