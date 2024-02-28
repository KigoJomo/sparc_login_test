#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Course, Task, Unit

class CustomUserCreationForm(UserCreationForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Select a course")
    reg_number = forms.CharField(max_length=20)
    year = forms.IntegerField()
    semester = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ("email", "reg_number","first_name","last_name", "course",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class TaskStatusForm(forms.Form):
    CHOICES = [('completed', 'Completed'), ('in_progress', 'In Progress'), ('delete', 'Delete')]
    status = forms.ChoiceField(choices=CHOICES)

class TaskSearchForm(forms.Form):
    search_term = forms.CharField(label='Search by title or unit')

class TaskCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.TextInput()
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Your Custom Placeholder'}))

    def __init__(self, user, *args, **kwargs):
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        # Filter units based on user's course
        self.fields['unit'].queryset = Unit.objects.filter(course=user.course, year=user.year, semester=user.semester)
        self.fields['unit'].empty_label = "Select"

    class Meta:
        model = Task
        fields = ('title', 'description', 'unit', 'due_date',)
