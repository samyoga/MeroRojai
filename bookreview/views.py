from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Book, Movie

def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books' : all_books
    }
    return render(request, 'bookreview/index.html', context)

def detail(request, book_id):
    return HttpResponse("<h2> details" + str(book_id) + "</h2>")
