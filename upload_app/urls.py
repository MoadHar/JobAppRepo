from django.urls import path 
from . import views

urlpatterns = [
path("", views.upload_image, name="u_upload_image"),
path("file", views.upload_file, name="u_upload_file"),
]