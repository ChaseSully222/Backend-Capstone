import sqlite3
from django.shortcuts import render
from baseballcardapp.models import Set
from ..connection import Connection

def set_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                s.id,
                s.name,
                s.year,
                s.notes
            from baseballcardapp_set s
            """)

            all_sets = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                set = Set()
                set.id = row['id']
                set.name = row['name']
                set.year = row['year']
                set.notes = row['notes']

                all_sets.append(set)
        template = 'sets/list.html'
        context = {
            'all_sets': all_sets
        }

        return render(request, template, context)