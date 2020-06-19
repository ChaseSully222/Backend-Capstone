import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import *
from ..connection import Connection


def get_sets():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Set)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            s.id,
            s.year,
            s.name,
            s.notes
        from baseballcardapp_set s
        """)

        return db_cursor.fetchall()

@login_required
def set_form(request):
    if request.method == 'GET':
        sets = get_sets()
        template = 'sets/form.html'
        context = {
            'all_sets': sets
        }

        return render(request, template, context)