#main app urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tasks/", views.tasks, name="tasks"),
    path("focus-hub/", views.focus_hub, name="focus-hub"),
    path("resources/", views.resources, name="resources"),
    path("performance/", views.performance, name="performance"),
]

