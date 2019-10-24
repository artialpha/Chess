import itertools
import json
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
        print("dziala post ")
        print(request.POST['open_name'])
        open_id = ChessOpening.objects.all().get(name=request.POST['open_name']).id
        dictionary = {'open_id': open_id}
        dictionary = json.dumps(dictionary)
        return HttpResponse(dictionary, content_type="application/json")

    return render(request, 'chess/list_chess_opening.html', context)


def chess_opening(request, open_id):
    chess_open = ChessOpening.objects.get(pk=open_id)
    list_of_positions = chess_open.create_chess_board(chess_open.epd)
    start_position = chess_open.start_position()

    context = {
        'name': chess_open.name,
        'description': chess_open.description,
        'eco': chess_open.eco,
        'position': list_of_positions,
        'start_position': start_position,
        'algebraic_notation': chess_open.number_to_algebraic()
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



    epd = 'rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/1PN2NP1/P3PPBP/R1BQ1RK1'

    mylist = create_chess_board(epd.split('/'))
    mylist = chess_dictionary(itertools.chain.from_iterable(mylist))

    context = {
        'position': mylist,
    }
    return render(request, 'chess/chess_board.html', context)


