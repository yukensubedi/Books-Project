from django.urls import path
from . import views
from books.views import *

urlpatterns = [
    path('add-author/', AuthorCreateView.as_view(), name='create_author'),
    path('add/', BooksCreateView.as_view(), name='create_book'),
    path('', BooksListView.as_view(), name='books_list'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),

]