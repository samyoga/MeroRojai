from django.http import Http404
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Book, Movie

def index(request):
    all_books = Book.objects.all()
    context = { 'all_books' : all_books }
    return render(request, 'bookreview/index.html', context)

def detail(request, book_id):
    try: 
        book = Book.objects.get( pk = book_id )
    except Book.DoesNotExist:
        raise Http404(" Book does not exist ")
    return render(request, 'bookreview/detail.html', {'book':book})