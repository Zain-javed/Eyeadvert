from django.shortcuts import render


def contactus(request):
    return render(request,'contact us.html')


def services(request):
    return render(request,'services.html')