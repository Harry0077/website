from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("iot-projects/", views.iot_projects, name="iot"),
    path("website-builds/", views.web_builds, name="web"),
    path("contact/", views.contact, name="contact"),
]
