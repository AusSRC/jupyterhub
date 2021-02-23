from django.db import models
from shops.models import Shop
 

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.FloatField()
    shop_id = models.ForeignKey(to=Shop, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'books'
