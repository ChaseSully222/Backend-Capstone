import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import *
from baseballcardapp.models import model_factory
from ..connection import Connection

def get_card(card_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Card)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.playerId_id,
            c.year,
            c.setId_id,
            c.cardNumber,
            c.imagePathFront,
            c.imagePathBack,
            c.attribute,
            pl.firstName firstName,
            pl.lastName lastName
        FROM baseballcardapp_card c
        JOIN baseballcardapp_player pl ON c.playerId_id = pl.id
        WHERE c.id = ?
        """, (card_id,))

        return db_cursor.fetchone()

@login_required
def card_details(request, card_id):
    if request.method == 'GET':
        card = get_card(card_id)

        template = 'cards/detail.html'
        context = {
            'card': card
        }

        return render(request, template, context)