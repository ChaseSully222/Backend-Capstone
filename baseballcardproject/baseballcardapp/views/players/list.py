import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import Player
from baseballcardapp.models import model_factory
from ..connection import Connection
from string import ascii_uppercase

playerCount = Player.objects.all().count()

def player_list(request):

    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Player)
            db_cursor = conn.cursor()
            letter = '%'
            if request.GET.get('letter', None) is not None:
                letter = f'{request.GET.get("letter", None)}%'
            else: 
                letter = '%'

            db_cursor.execute("""
            SELECT
                p.firstName,
                p.lastName,
                p.id
            FROM baseballcardapp_player p
            WHERE lastName LIKE ?
            """, (letter,))

            all_players = db_cursor.fetchall()
            print(all_players)
            # If a letter is provided as a query parameter, then filter list of players last name by letter

            # letter = request.GET.get('letter', None)
            # if letter is not None:
            #     all_players(letter=letter)
                
            # elif letter is None:
            #     all_players

        template = 'players/list.html'
        context = {
            'all_players': all_players,
            'alphabet': ascii_uppercase
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

