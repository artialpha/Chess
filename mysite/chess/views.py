import itertools
import json
from django.http import HttpResponse
from django.shortcuts import render
from mysite import settings
from django.views.decorators.csrf import csrf_exempt
from .models import ChessOpening
from .forms import ChessOpeningForm


def index(request):
    return render(request, 'mysite/index.html', {})


def nothing(request):
    string = settings.STATIC_ROOT
    return HttpResponse(string)


def create_chess_opening(request):
    form = ChessOpeningForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'chess/create_chess_opening.html', context)


def list_chess_opening(request):
    a_open = ChessOpening.objects.order_by('eco').filter(eco__contains='A')
    b_open = ChessOpening.objects.order_by('eco').filter(eco__contains='B')
    c_open = ChessOpening.objects.order_by('eco').filter(eco__contains='C')
    d_open = ChessOpening.objects.order_by('eco').filter(eco__contains='D')
    e_open = ChessOpening.objects.order_by('eco').filter(eco__contains='E')

    chess_open = [
        {'open': a_open, 'text': "group A"},
        {'open': b_open, 'text': "group B"},
        {'open': c_open, 'text': "group C"},
        {'open': d_open, 'text': "group D"},
        {'open': e_open, 'text': "group E"},
    ]

    context = {
        'chess_open': chess_open,
        'a_open': a_open,
        'b_open': b_open,
        'c_open': c_open,
        'd_open': d_open,
        'e_open': e_open,
    }

    if request.method == 'POST':
        open_id = ChessOpening.objects.all().get(name=request.POST['open_name']).id
        dictionary = {'open_id': open_id}
        dictionary = json.dumps(dictionary)
        return HttpResponse(dictionary, content_type="application/json")

    return render(request, 'chess/list_chess_opening.html', context)


def chess_opening(request, open_id):
    chess_open = ChessOpening.objects.get(pk=open_id)
    list_of_positions = ChessOpening.create_chess_board(chess_open.epd)
    start_position = ChessOpening.start_position()

    context = {
        'name': chess_open.name,
        'description': chess_open.description,
        'eco': chess_open.eco,
        'position': list_of_positions,
        'start_position': start_position,
        'algebraic_notation': chess_open.number_to_algebraic()
    }
    return render(request, 'chess/single_chess_opening.html', context)


@csrf_exempt
def chess_board(request):
    if request.method == 'POST':
        print(request.POST['epd'])
        list_of_positions = ChessOpening.create_chess_board(request.POST['epd'])
        list_of_positions = json.dumps(list_of_positions)
        return HttpResponse(list_of_positions, content_type="application/json")

    context = {

    }
    return render(request, 'chess/chess_board_epd.html', context)


