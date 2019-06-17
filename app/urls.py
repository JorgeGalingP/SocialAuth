from django.urls import path,include
from django.contrib.auth import views as auth_views
from app import views
from django.contrib import admin

urlpatterns = [
    path('home/',views.home),
    path('social-auth/',include('social_django.urls',namespace="social")),
    path('login/',views.login),
    path('logout/',auth_views.LogoutView.as_view()),

]
