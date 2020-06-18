from django.contrib.auth.decorators import login_required
import sqlite3
from django.shortcuts import render
from baseballcardapp.models import Collection
from ..connection import Connection


@login_required
def collection_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.userId_id,
                c.cardId_id,
                c.notes
            FROM baseballcardapp_collection c
            """)

            all_collections = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                collection = Collection()
                collection.id = row['id']
                collection.userId_id = row['userId_id']
                collection.cardId_id = row['cardId_id']
                collection.notes = row['notes']

                all_collections.append(collection)

        template = 'collection/list.html'
        context = {
            'all_collections': all_collections
        }

        return render(request, template, context)