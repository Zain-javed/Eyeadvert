from django.shortcuts import render,get_object_or_404
from .models import Billboard
from .models import Outdoor


def billboard(request):
    billadd= Billboard.objects.all()

    return render(request,'billboard.html',{'billadd':billadd } )


def boarddetail(request,advertise_id):
    detailboard=get_object_or_404(Billboard,pk=advertise_id)

    return render(request,'detailboard.html',{'detailboard': detailboard})


def outdoor(request):
    outadd=Outdoor.objects.all()

    return render(request,'outdoor.html',{'outadd':outadd})


def outdetail(request,advertise_id):
    detailout=get_object_or_404(Outdoor,pk=advertise_id)

    return render(request,'detailout.html',{'detailout': detailout})