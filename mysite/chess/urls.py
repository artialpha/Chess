from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:open_id>/', views.chess_opening, name='open'),
    path('nothing/', views.nothing, name='nothing')
]