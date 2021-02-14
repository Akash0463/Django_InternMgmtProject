from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('register1', views.register1, name='register1'),
    path('loginView', views.loginView, name='loginView'),
    path('validateLogin', views.validateLogin, name='validateLogin'),
    path('displaySubPost', views.displaySubPost, name='displaySubPost'),
    path('apply', views.apply, name='apply'),
    path('addApplicantDetails', views.addApplicantDetails, name='addApplicantDetails'),
    path('retrieveData', views.retrieveData, name='retrieveData'),
    path('displayJobPosting', views.displayJobPosting, name='displayJobPosting'),
    path('logout', views.logout, name='logout')
]

