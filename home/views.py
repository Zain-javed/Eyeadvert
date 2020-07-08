from django.shortcuts import render
from blog.models import Blog
from .models import Recommend
from advertise.models import Billboard
from advertise.models import Outdoor


def home(request):

    context = {
         'recommend': Recommend.objects,
         'billadd' : Billboard.objects,
          'outadd' : Outdoor.objects,
        'allblog': Blog.objects.filter()[:3]
    }
    return render(request,'home1.html',context)
# Create your views here.
