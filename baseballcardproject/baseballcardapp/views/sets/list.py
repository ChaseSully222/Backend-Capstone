import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from ..connection import Connection

def set_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Set)
            db_cursor = conn.cursor()
            year = '%'
            if request.GET.get('year', None) is not None:
                year = f'{request.GET.get("year", None)}%'
            else: 
                year = '%'

            db_cursor.execute("""
            SELECT
                s.id,
                s.name,
                s.year,
                s.setnotes
            FROM baseballcardapp_set s
            WHERE year LIKE ?
            """, (year,))

            all_sets = db_cursor.fetchall()

            db_cursor.execute("""
            SELECT DISTINCT
                s.year
            FROM baseballcardapp_set s
            """)

            all_years = db_cursor.fetchall()

        template = 'sets/list.html'
        context = {
            'all_sets': all_sets,
            'all_years': all_years
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

def year_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Set)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT
                s.year
            FROM baseballcardapp_set s
            """)

            all_years = db_cursor.fetchall()

        template = 'sets/list.html'
        context = {
            'all_years': all_years
        }

        return render(request, template, context)