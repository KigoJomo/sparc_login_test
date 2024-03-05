#project level urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="main/home.html"), name="home"),
]
