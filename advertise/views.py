from django.shortcuts import render,get_object_or_404
from .models import Billboard


def billboard(request):
    billadd= Billboard.objects.all()

    return render(request,'billboard.html',{'billadd':billadd } )


def boarddetail(request,advertise_id):
    detailboard=get_object_or_404(Billboard,pk=advertise_id)

    return render(request,'detailboard.html',{'detailboard': detailboard})
