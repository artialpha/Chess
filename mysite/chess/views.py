from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def nothing(request):
    return HttpResponse("completely nothing" )


def chess_opening(request, open_id):
    return HttpResponse("You're looking at question %s." % open_id)