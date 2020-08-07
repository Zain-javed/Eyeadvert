from django.db import models


class Billboard(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=50)
    description=models.TextField(max_length=600,default='')
    Category=models.CharField(max_length=30,default='Outdoor')
    Company=models.CharField(max_length=60,default='')
    Medium = models.CharField(max_length=60,default='Print Medium')
    price = models.IntegerField(default=500)
    availability = models.CharField(max_length=50,default='Available')
    Phone=models.CharField(max_length=30,default='+92')
    Areacoverd= models.CharField(max_length=100,default='Fotress')
    facebook=models.CharField(max_length=100,default='https://www.facebook.com/EyeAdvert-111649233951911')
    insta=models.CharField(max_length=100,default='https://www.instagram.com/?hl=en')


    def __str__(self):
       return self.name


class Outdoor(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=600, default='')
    Category = models.CharField(max_length=30, default='Outdoor')
    Company=models.CharField(max_length=60,default='')
    Medium = models.CharField(max_length=60, default='Print Medium')
    price = models.IntegerField(default=500)
    availability = models.CharField(max_length=50, default='Available')
    Phone = models.CharField(max_length=30, default='+92')
    Areacoverd = models.CharField(max_length=100, default='Fotress')
    facebook = models.CharField(max_length=100, default='https://www.facebook.com/EyeAdvert-111649233951911')
    insta = models.CharField(max_length=100, default='https://www.instagram.com/?hl=en')

    def __str__(self):
        return self.name

# Create your models here.
