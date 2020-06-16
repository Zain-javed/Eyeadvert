from django.db import models


class Recommend(models.Model):

    image = models.ImageField(upload_to='img/')
    summary= models.CharField(max_length=100)

# Create your models here.
