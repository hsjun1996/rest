"""Restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import reservation.views

urlpatterns = [
    path('', reservation.views.reservation, name='reservation'),
    path('reservation_check/',reservation.views.reservation_check, name='reservation_check'),
    path('reservation_button/',reservation.views.reservation_button, name='reservation_button'),
    path('reservation_check/<int:id>', reservation.views.reservation_delete, name='reservation_delete'),
    path('reservation_update/<int:id>', reservation.views.reservation_update, name='reservation_update'),
 
]
