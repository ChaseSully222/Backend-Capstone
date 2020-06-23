from django.contrib.auth.decorators import login_required
import sqlite3
from django.shortcuts import render, redirect, reverse
from baseballcardapp.models import *
from ..connection import Connection


def collection_details(request, collection_id):
    form_data = request.POST  
    
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