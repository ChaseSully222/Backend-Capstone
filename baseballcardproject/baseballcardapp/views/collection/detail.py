from django.contrib.auth.decorators import login_required
import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from ..connection import Connection

def get_collection(collection_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Collection)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.cardId_id,
            c.userId_id,
            c.notes
        FROM baseballcardapp_collection c
        WHERE c.id = ?
        """, (collection_id,))

        return db_cursor.fetchone()


def collection_details(request, collection_id):
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE baseballcardapp_collection
                SET notes = ?
                WHERE id = ?
                """,
                (
                    form_data['notes'], collection_id
                ))

        return redirect(reverse('baseballcardapp:mycollection'))


        # Check if this POST is for deleting a card in collection
    
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                DELETE FROM baseballcardapp_collection
                WHERE id = ?
                """, (collection_id,))

            return redirect(reverse('baseballcardapp:mycollection'))


@login_required
def collection_edit_form(request, collection_id):

    if request.method == 'GET':
        collection = get_collection(collection_id)

        template = 'collection/form.html'
        context = {
            'collection': collection,
        }

        return render(request, template, context)