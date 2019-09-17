from django.http import HttpResponse
from django.shortcuts import render
from mysite import settings
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
    chess_open = ChessOpening.objects.order_by('eco').all()
    context = {
        'chess_open': chess_open
    }

    return render(request, 'chess/list_chess_opening.html', context)


def chess_opening(request, open_id):
    chess_open = ChessOpening.objects.get(pk=open_id)
    context = {
        'name': chess_open.name,
        'description': chess_open.description,
        'eco': chess_open.eco
    }
    return render(request, 'chess/single_chess_opening.html', context)


