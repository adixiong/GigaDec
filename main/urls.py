from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("about-us/", views.aboutUs, name="about-us"),
    path("web-client/", views.webClient, name="web-client"),
    path("mobile/", views.mobile, name="mobile"),
    path("pricing/", views.pricing, name="pricing"),
]