from django.http import HttpResponse
from django.shortcuts import render
from uuid import uuid4
from book.models import Book


# Create your views here.


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, 'book/index.html', context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    # select * from book where id = pk
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context)


