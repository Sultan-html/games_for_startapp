from django.urls import path
from apps.games.views import game

urlpatterns = [
    path('', game, name='index'),
]
