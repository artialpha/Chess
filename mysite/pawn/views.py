from django.shortcuts import render

# Create your views here.

def pawn(request):
    return render(request, 'pawn/pawn.html', {})
