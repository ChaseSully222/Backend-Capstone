from django.contrib.auth.decorators import login_required
import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from ..connection import Connection


@login_required
def collection_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Collection)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.userId_id,
                c.cardId_id,
                c.notes,
                ca.year year,
                ca.setId_id,
                ca.playerId_id,
                ca.cardNumber cardNumber,
                ca.attribute attribute,
                pl.lastName lastName,
                pl.firstName firstName,
                se.name name
            FROM baseballcardapp_collection c
            JOIN baseballcardapp_card ca on c.cardId_id = ca.id
            JOIN baseballcardapp_set se on ca.setId_id = se.id
            JOIN baseballcardapp_player pl on ca.playerId_id = pl.id
            """)

            all_collections = db_cursor.fetchall()

        template = 'collection/list.html'
        context = {
            'all_collections': all_collections
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST  

        user = request.user
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO baseballcardapp_collection
            (
                cardId_id, userId_id
            )
            VALUES (?,?)
            """,
            (form_data['card_id'], user.id))

        return redirect(reverse('baseballcardapp:players'))
