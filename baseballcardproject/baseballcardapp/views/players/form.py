import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import model_factory, Player
from ..connection import Connection


def get_players():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Player)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.firstName,
            p.lastName  
        FROM baseballcardapp_player p
        """)

        return db_cursor.fetchall()


@login_required
def player_form(request):

    if request.method == 'GET':
        players = get_players()
        template = 'players/form.html'
        context = {
            'all_players': players
        }
        return render(request, template, context)