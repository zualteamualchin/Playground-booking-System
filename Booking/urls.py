from os import name
from django.urls import path

from . import views
from .forms import CustomerForm

urlpatterns = [
    path('', views.index, name="index"),
    path('indoor', views.indoor, name="indoor"),
    path('outdoor', views.outdoor, name='outdoor'),
    path('location', views.location, name='children'),
    path('location', views.location, name='location'),
    path('teams', views.teams, name='teams'),
    path('login', views.loginUser, name='loginUser'),
    path('booking', views.book, name="booking"),
    path('register', views.register, name="register"),
    path('billing', views.bills, name="bills"),
    path('managerLogin', views.managerLogin, name="managerLogin"),
    path('Customerprofile', views.CustomerProfile, name="CustomerProfile"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('CustomerBookingHistory', views.CustomerBookingHistory, name="CustomerBookingHistory"),
    path('CustomerTransactionHistory', views.CustomerTransactionHistory, name="CustomerTransactionHistory"),
    path('Privacy', views.Privacy, name="Privacy"),
    path('CustomerProfileSettings', views.CustomerProfileSettings, name="CustomerProfileSettings"),
    path('ManagerProfile', views.ManagerProfile, name='ManagerProfile')
    
]