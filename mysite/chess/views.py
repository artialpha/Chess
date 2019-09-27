import itertools

from django.http import HttpResponse
from django.shortcuts import render
from mysite import settings
from .models import ChessOpening
from .forms import ChessOpeningForm
import re


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


def chess_board(request):

    def translate(char):
        if char == 'k':
            return '&#9818;'
        if char == 'q':
            return '&#9819;'
        if char == 'r':
            return '&#9820;'
        if char == 'b':
            return '&#9821;'
        if char == 'n':
            return '&#9822;'
        if char == 'p':
            return '&#9823;'

        if char == 'K':
            return '&#9812;'
        if char == 'Q':
            return '&#9813;'
        if char == 'R':
            return '&#9814;'
        if char == 'B':
            return '&#9815;'
        if char == 'N':
            return '&#9816;'
        if char == 'P':
            return '&#9817;'

    def get_position(string, line):
        uni = 97
        index = 0
        list_out = []
        for char in string:
            # print(char)
            if char.isdigit():
                index += int(char)
            else:
                list_out.append((chr(index + uni), line, translate(char)))
                index += 1 if index < 8 else index
        return list_out

    def create_chess_board(epd):
        mylist = []
        for index, line in enumerate(epd):
            mylist.append(get_position(line, 8 - index))

        return mylist

    def chess_dictionary(mylist):
        dictionary = {}
        for i in mylist:
            # print(i)
            dictionary[i[0].capitalize() + str(i[1])] = i[2]
        return dictionary


    position2 = {
        "A8": "&#9820;",
        "B8": "&#9822;",
        "C8": "&#9821;",
        "D8": "&#9819;",
        "E8": "&#9818;",
        "F8": "&#9821;",
        "G8": "&#9822;",
        "H8": "&#9820;",

        "A7": "&#9823;",
        "B7": "&#9823;",
        "C7": "&#9823;",
        "D7": "&#9823;",
        "E7": "&#9823;",
        "F7": "&#9823;",
        "G7": "&#9823;",
        "H7": "&#9823;",

        "A1": "&#9814;",
        "B1": "&#9816;",
        "C1": "&#9815;",
        "D1": "&#9813;",
        "E1": "&#9812;",
        "F1": "&#9815;",
        "G1": "&#9816;",
        "H1": "&#9814;",

        "A2": "&#9817;",
        "B2": "&#9817;",
        "C2": "&#9817;",
        "D2": "&#9817;",
        "E2": "&#9817;",
        "F2": "&#9817;",
        "G2": "&#9817;",
        "H2": "&#9817;",
    }

    epd = 'rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/1PN2NP1/P3PPBP/R1BQ1RK1'

    mylist = create_chess_board(epd.split('/'))
    mylist = chess_dictionary(itertools.chain.from_iterable(mylist))

    context = {
        'position': mylist,
    }
    return render(request, 'chess/chess_board.html', context)


