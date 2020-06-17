from django.db import models


class Billboard(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=500)

    def __str__(self):
       return self.name


# Create your models here.
