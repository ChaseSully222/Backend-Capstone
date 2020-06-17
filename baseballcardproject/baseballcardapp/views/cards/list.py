import sqlite3
from django.shortcuts import render
from baseballcardapp.models import Card
from ..connection import Connection

def card_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.playerId,
                c.year,
                c.setId,
                c.imagePathFront,
                c.cardNumberBack,
                c.attribute
            from baseballcardapp_card c
            """)

            all_cards = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                card = Card()
                card.playerId = row['playerId']
                card.year = row['year']
                card.setId = row['setId']
                card.imagePathFront = row['imagePathFront']
                card.imagePathBack = row['imagePathBack']
                card.cardNumber = row['cardNumber']
                card.attribute = row['attribute']

                all_cards.append(card)

        template = 'cards/list.html'
        context = {
            'all_cards': all_cards
        }

        return render(request, template, context)