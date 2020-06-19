import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import Player
from baseballcardapp.models import model_factory
from ..connection import Connection

playerCount = Player.objects.all().count()


def player_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.firstName,
                p.lastName
            from baseballcardapp_player p
            """)

            all_players = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                player = Player()
                player.firstName = row['firstName']
                player.lastName = row['lastName']

                all_players.append(player)

        template = 'players/list.html'
        context = {
            'all_players': all_players
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO baseballcardapp_player
            (
                firstName,lastName
            )
            VALUES (?, ?)
            """,
            (form_data['firstName'], form_data['lastName']))

            return redirect(reverse('baseballcardapp:players'))

