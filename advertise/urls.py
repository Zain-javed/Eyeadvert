from django.urls import path
from advertise import views

urlpatterns = [
    path('billboard',views.billboard,name='billboard'),
    path('<int:advertise_id>/',views.boarddetail,name='boarddetail')

]