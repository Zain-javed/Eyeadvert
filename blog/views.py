from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def blogs(request):


    allblog = Blog.objects.all()
    p = Paginator(allblog, 12)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    # return render(request, 'list.html', {'page_obj': page_obj})

    return render(request,'blog.html', {'allblog' : page_obj})

def detail(request,blog_id):

    detailblog= get_object_or_404(Blog,pk=blog_id)

    return render(request,'blog-details.html',{'detailblog': detailblog})

# Create your views here.
