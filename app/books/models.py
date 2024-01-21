from django.db import models


class Author(models.Model):
    """ 
    Models for author 
    """
    author_name = models.CharField(max_length=255)
    def __str__(self):
        return self.author_name


class Books(models.Model):
    """ 
    Models for books 
    """
    book_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.book_name



