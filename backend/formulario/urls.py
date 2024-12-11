from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path(route="formulario/", view=views.UserFormView.as_view(), name="formulario"), 
]
