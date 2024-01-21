from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import *

# Create your views here.
def test(request):
    return render(request, 'index.html')
class AuthorCreateView(View):
    """
    Views to create a new author 
    """
    template_name = 'create_author.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        author_name = request.POST.get('author_name')
        Author.objects.create(
            author_name=author_name
        )
        return HttpResponse('New Author created Successfully')

class BooksCreateView(View):
    """
    Views to add books to database 
    """
    template_name = 'book_create.html'

    def get(self, request):
        authors = Author.objects.all()
        context = {'authors': authors}
        return render(request, self.template_name, context)
    
    def post(self, request):
        book_name = request.POST.get('book_name')
        price = request.POST.get('price')
        author_id = request.POST.get('author')

        author = Author.objects.get(pk=author_id)
        Books.objects.create(
            book_name=book_name,
            price=price,
            author=author
        )
        return redirect('books_list')

class BookDetailView(View):
    """
    View to see details of a book 
    """

    template_name = 'book_detail.html'

    def get(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        context = {'book': book}
        return render(request, self.template_name, context)

class BooksListView(View):
    """
    View for listing books  
    """

    template_name = 'books_list.html'

    def get(self, request):
        books = Books.objects.all()
        context = {'books':books}
        return render(request, self.template_name, context)

class BookUpdateView(View):
    """
    View for updating books information 
    """

    template_name = 'book_create.html'

    def get(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        authors = Author.objects.all()
        context = {'book': book, 'authors': authors}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        
        # Update book attributes
        book.book_name = request.POST.get('book_name')
        book.price = request.POST.get('price')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, pk=author_id)
        
        book.save()

        return redirect('books_list')

class BookDeleteView(View):
    """
    View to delete the particular book 
    """
    template_name = 'books_list.html'

    def post(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        book.delete()
        return redirect('books_list')
    
     
