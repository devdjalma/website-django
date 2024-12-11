from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path(
        route="registrados/", view=views.RegistradosView.as_view(), name="registrados"
    ),
    path(route="home/", view=views.home, name="home"),
]
