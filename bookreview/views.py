from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse ("hello")

def detail(request, book_id):
    return HttpResponse("<h2> details" + str(book_id) + "</h2>")
