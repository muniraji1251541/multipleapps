from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('file1/',file1,name='file1'),
    path('file2/',file2,name='file2'),
]