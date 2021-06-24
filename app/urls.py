from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.base,name='base'),
    path('form',views.form,name='form'),
    path('search',views.search,name="search"),
    path('student',views.student,name="student"),


]