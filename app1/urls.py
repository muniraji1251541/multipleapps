from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('fun1/',fun1,name='fun1'),
    path('fun2/',fun2,name='fun2'),
]