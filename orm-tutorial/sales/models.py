from django.db import models
from books.models import Book
from stores.models import Store


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, to_field='id', on_delete=models.DO_NOTHING)
    store = models.ForeignKey(Store, to_field='id', on_delete=models.DO_NOTHING)
    sold_at = models.DateTimeField(auto_now=True)
