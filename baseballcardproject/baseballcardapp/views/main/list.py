import sqlite3
from django.shortcuts import render
from baseballcardapp.models import Card
from baseballcardapp.models import Set
from ..connection import Connection

def main(request):
    if request.method == 'GET':
        template = 'main.html'
        context = {}

        return render(request, template, context)