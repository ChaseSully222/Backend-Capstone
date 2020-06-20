import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import *
from baseballcardapp.models import model_factory
from ..connection import Connection


def get_player(playerId):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Player)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.firstName,
            p.lastName
        FROM baseballcardapp_player p
        WHERE p.id = ?
        """, (playerId,))

        return db_cursor.fetchone()

@login_required
def player_details(request, playerId):
    if request.method == 'GET':
        player = get_player(playerId)

        template = 'players/detail.html'
        context = {
            'player': player
        }

        return render(request, template, context)