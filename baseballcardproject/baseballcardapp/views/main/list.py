import sqlite3
from django.shortcuts import render
from baseballcardapp.models import Card
from baseballcardapp.models import Set
from baseballcardapp.models import Player
from ..connection import Connection

def main(request):

    playerCount = Player.objects.all().count()
    cardCount = Card.objects.all().count()
    setCount = Set.objects.all().count()

    if request.method == 'GET':
        template = 'main.html'
        context = {
            'playerCount': playerCount,
            'cardCount': cardCount,
            'setCount': setCount
        }

        return render(request, template, context)