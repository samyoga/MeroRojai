from django.shortcuts import HttpResponse
from django.template import loader
from .models import Book, Movie

def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('bookreview/index.html')
    context = {
        'all_books' : all_books
    }
    return HttpResponse (template.render(context,request))

def detail(request, book_id):
    return HttpResponse("<h2> details" + str(book_id) + "</h2>")
