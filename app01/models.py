from django.db import models

# Create your models here.

class Book_single(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.CharField(max_length=128)

    def __str__(self):
        return self.title