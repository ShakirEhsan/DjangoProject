from django.urls import path 
from core1 import views

urlpatterns = [
    path('stu/', views.studentinfo),
]