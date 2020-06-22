import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from baseballcardapp.models import *
from ..connection import Connection


def get_set(set_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Set)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.year,
            s.name,
            s.setnotes
        FROM baseballcardapp_set s
        WHERE s.id = ?
        """, (set_id,))

        return db_cursor.fetchone()

@login_required
def set_details(request, set_id):
    if request.method == 'GET':
        set = get_set(set_id)

        template = 'sets/detail.html'
        context = {
            'set': set
        }

        return render(request, template, context)