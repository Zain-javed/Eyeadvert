from django.shortcuts import render
from blog.models import Blog
from .models import Recommend


def home(request,):
    recommend= Recommend.objects
    context = {
         'recommend':Recommend.objects,
        'allblog': Blog.objects.filter()[:4]
    }
    return render(request,'home1.html',context)
# Create your views here.
