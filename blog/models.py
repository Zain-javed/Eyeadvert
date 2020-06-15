from django.db import models

from django.db import models


class Blog(models.Model):
    image= models.ImageField (upload_to='blog/')
    author_img = models.ImageField(upload_to='blog/',default='blog/')
    date = models.DateTimeField()
    category = models.CharField(max_length=80, default='Unknown')
    summary = models.CharField(max_length= 80)
    company = models.CharField(max_length=80, default='Unknown')
    text = models.TextField (max_length= 200)
    Comment= models. IntegerField (default=1)
    blogger= models.CharField(max_length= 80,default= 'Unknown')
    facebook_link=models.CharField (max_length= 80,default='https://www.facebook.com/tickabrand/')
    insta_link=models.CharField (max_length= 80,default='https://www.instagram.com/tickabrand/')




    def __str__(self):
        return self.summary


    def date_pretty(self):
        return self.date.strftime('%b %e %Y')

    def text_pretty(self):
        return self.text[:50]






# Create your models here.
