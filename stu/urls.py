from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('getCourseList', views.getCourseList),
    path('markMe', views.markMe),
    path('getStats', views.getStats),
]