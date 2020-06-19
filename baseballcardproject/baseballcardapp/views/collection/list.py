from django.contrib.auth.decorators import login_required
import sqlite3
from django.shortcuts import render
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
                c.notes
            FROM baseballcardapp_collection c
            """)

            all_collections = db_cursor.fetchall()

        template = 'collection/list.html'
        context = {
            'all_collections': all_collections
        }

        return render(request, template, context)