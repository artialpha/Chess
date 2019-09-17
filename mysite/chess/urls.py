from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:open_id>/', views.chess_opening, name='open'),
    path('nothing/', views.nothing, name='nothing'),
    path('create-opening/', views.create_chess_opening, name='create opening'),
    path('list-opening/', views.list_chess_opening, name='list openings'),
]

