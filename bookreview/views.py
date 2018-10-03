from django.shortcuts import HttpResponse
from .models import Book, Movie

def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/bookreview/' + str(book.id) + '/'
        html += '<a href="' + url + '">' + book.book_title + '</a><br>'
    return HttpResponse (html)

def detail(request, book_id):
    return HttpResponse("<h2> details" + str(book_id) + "</h2>")
