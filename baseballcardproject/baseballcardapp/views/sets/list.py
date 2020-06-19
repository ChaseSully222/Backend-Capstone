import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from ..connection import Connection

def set_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Set)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                s.id,
                s.name,
                s.year,
                s.setnotes
            from baseballcardapp_set s
            """)

            all_sets = db_cursor.fetchall()

        template = 'sets/list.html'
        context = {
            'all_sets': all_sets
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO baseballcardapp_set
            (
                year, name, setnotes
            )
            VALUES (?, ?, ?)
            """,
            (form_data['year'], form_data['name'],
                form_data['setnotes']))

        return redirect(reverse('baseballcardapp:sets'))