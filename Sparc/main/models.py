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
    focus_period = models.IntegerField(default=25) #in minutes
    break_duration = models.IntegerField(default=5) #in minutes
    daily_goal = models.IntegerField(default=4) #in hours
    streak = models.IntegerField(default=0)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Unit(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()
    outline = models.TextField(null=True)


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
    grade = models.CharField(max_length=2, null=True)


class Resource(models.Model):
    name = models.CharField(unique=True, max_length=250)
    file_attachment = models.FileField(upload_to="resource_attachments")
    unit = models.CharField(max_length=200, null=True)


class ImportantDate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Session(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session_duration_mins = models.IntegerField()
    session_duration_sec = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    goal = models.IntegerField() #in hours
