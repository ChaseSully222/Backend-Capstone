import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from baseballcardapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def card_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Card)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.playerId,
                c.year,
                c.setId,
                c.cardNumber,
                c.imagePathFront,
                c.imagePathBack,
                c.attribute
            from baseballcardapp_card c
            """)

            all_cards = db_cursor.fetchall()

        template = 'card/list.html'
        context = {
            'all_cards': all_cards
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO baseballcardapp_card
            (
                playerId_id, year, setId_id, cardNumber, imagePathFront, ImagePathBack, attribute
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data["player"], form_data['year'],
                form_data["set"], form_data['cardNumber'],
                form_data['imagePathFront'], form_data['imagePathBack'],
                form_data['attribute']))

        return redirect(reverse('baseballcardapp:main'))