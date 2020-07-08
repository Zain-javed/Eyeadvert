from django.urls import path
from info import views

urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]