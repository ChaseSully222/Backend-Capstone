import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import Player
from baseballcardapp.models import Set
from baseballcardapp.models import Card
from baseballcardapp.models import model_factory
from ..connection import Connection


def get_players():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Player)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            p.id,
            p.firstName,
            p.lastName
        from baseballcardapp_player p
        """)

        return db_cursor.fetchall()

def get_sets():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Set)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            s.id,
            s.name,
            s.year,
            s.notes
        from baseballcardapp_set s
        """)

        return db_cursor.fetchall()

@login_required
def card_form(request):
    if request.method == 'GET':
        players = get_players()
        sets = get_sets()
        template = 'cards/form.html'
        context = {
            'all_players': players,
            'all_sets': sets
        }

        return render(request, template, context)