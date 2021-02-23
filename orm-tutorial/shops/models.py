from django.db import models


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    state = models.TextField(max_length=10)
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'shops'