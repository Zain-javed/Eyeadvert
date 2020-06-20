from django.db import models


class Billboard(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=50)
    description=models.TextField(max_length=300,default='')
    Category=models.CharField(max_length=30,default='Outdoor')
    price = models.IntegerField(default=500)
    availability = models.CharField(max_length=50,default='Available')
    Phone=models.CharField(max_length=30,default='+92')
    Areacoverd= models.CharField(max_length=30,default='Fotress')
    facebook=models.CharField(max_length=30,default='http://')
    insta=models.CharField(max_length=30,default='http://')


    def __str__(self):
       return self.name


class Outdoor(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, default='')
    Category = models.CharField(max_length=30, default='Outdoor')
    price = models.IntegerField(default=500)
    availability = models.CharField(max_length=50, default='Available')
    Phone = models.CharField(max_length=30, default='+92')
    Areacoverd = models.CharField(max_length=30, default='Fotress')
    facebook = models.CharField(max_length=30, default='http://')
    insta = models.CharField(max_length=30, default='http://')

    def __str__(self):
        return self.name

# Create your models here.
