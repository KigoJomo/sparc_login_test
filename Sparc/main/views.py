from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
