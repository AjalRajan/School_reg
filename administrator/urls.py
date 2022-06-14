
from django.contrib import admin
from django.urls import path
from administrator.views import *

urlpatterns = [

    path('', Home.as_view() , name = "home"),
    path('add_stu/' , Addstd.as_view() , name='addstud'),
    path('update_stu/<int:pk>/' , Updatestd.as_view() , name='updatestud'),
    path('delete_stu/<int:pk>/' , Deletestu.as_view() , name='deletestud'),
    
]
