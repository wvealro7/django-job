from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list,name='list'),
    path('detail/<str:slug>', views.job_detail,name='details'),
]