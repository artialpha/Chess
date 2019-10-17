from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:open_id>/', views.chess_opening, name='open'),
    path('nothing/', views.nothing, name='nothing'),
    path('create-opening/', views.create_chess_opening, name='create opening'),
    path('list-opening/', views.list_chess_opening, name='list openings'),
    path('chess-board/', views.chess_board, name='chess board'),
]

