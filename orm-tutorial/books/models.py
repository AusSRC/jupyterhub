from django.db import models
from stores.models import Store
 

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.FloatField()
    store = models.ForeignKey(Store, to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
