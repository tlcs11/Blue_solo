from django.urls import path

# from . import views

from .views import family, directory_view, add_family, delete_family

urlpatterns = [
    path("", family, name="family-home"),
    path("directory", directory_view, name="directory"),
    path("add", add_family, name="add"),
    path("delete", delete_family, name="delete"),
]

