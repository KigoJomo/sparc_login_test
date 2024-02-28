from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class Course(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=250)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    reg_number = models.CharField(max_length=20, unique=True, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default="C025")
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Unit(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()


class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()


class Performance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    score = models.IntegerField()


class Resource(models.Model):
    name = models.CharField(unique=True, max_length=250)
    file_attachment = models.FileField(upload_to="resource_attachments", null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class ImportantDate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
