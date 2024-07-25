from django.contrib import admin
from django.urls import path
from book.views import book_list, book_detail

urlpatterns = [
    path('book-list/', book_list, name='book_list'),
    path('book-detail/<int:book_id>', book_detail, name='book_detail')
]
