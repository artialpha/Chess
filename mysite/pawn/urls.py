from django.urls import path
from . import views


urlpatterns = [
    path('pawns', views.pawn, name='pawns'),
]

