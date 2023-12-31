
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.pets_register, name="pets_register"),
    path("login/", views.pets_login, name="pets_login"),
    path("logout/", views.pets_logout, name="pets_logout"),
    path("playlist/", views.playlist, name="playlist"),

]
