from django.urls import path

# from . import views

from .views import family, directory_view, add_family, delete_family, update_family

urlpatterns = [
    path("", family, name="family-home"),
    path("directory", directory_view, name="directory"),
    path("add", add_family, name="add"),
    path("delete/<int:id>", delete_family, name="delete"),
    path("update/<int:id>", update_family, name="update")
]

