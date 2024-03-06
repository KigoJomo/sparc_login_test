#views.py
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, ImportantDate, Performance, Task, Unit, Session, CustomUser, Resource
from .forms import CustomUserCreationForm, TaskSearchForm, TaskCreationForm, TaskStatusForm, SessionCreateForm, FocusSettingsForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

    def form_valid(self, form):
        # Get the course_code from the form data
        course = self.request.POST.get('course')

        # Convert the course_code to a Course instance
        course_instance = get_object_or_404(Course, code=course)

        # Assign the Course instance to the CustomUser's course_code field
        form.instance.course = course_instance

        return super().form_valid(form)

@login_required(login_url='login/')
def dashboard(request):
    upcoming_dates = ImportantDate.objects.filter(date__gte=timezone.now())
    user = request.user
    user_years = list(range(1, user.year + 1))
    user_semesters = list(range(1, user.semester + 1))
    performances = Performance.objects.filter(user=user.reg_number)

    context = {
        'upcoming_dates': upcoming_dates,
        'performances': performances,
        'user_years': user_years,
        'user_semesters': user_semesters,
    }
    return render(request, 'main/dashboard.html', context)

@login_required(login_url='login/')
def tasks(request):
    user = request.user
    search_form = TaskSearchForm()
    create_form = TaskCreationForm(user=request.user)
    task_status_form = TaskStatusForm()
    tasks = Task.objects.filter(user=user.reg_number).order_by('-created_at')

    if request.method == 'POST':
        if 'search_form_submit' in request.POST:
            search_form = TaskSearchForm(request.POST)
            if search_form.is_valid():
                search_term = search_form.cleaned_data['search_term']
                if search_term:
                    tasks = tasks.filter(Q(title__icontains=search_term) | Q(unit__name__icontains=search_term)).order_by('-created_at')
        elif 'create_form_submit' in request.POST:
            create_form = TaskCreationForm(request.user, request.POST)
            if create_form.is_valid():
                task = Task(
                    title=create_form.cleaned_data['title'],
                    user = user,
                    description = create_form.cleaned_data['description'],
                    unit = create_form.cleaned_data['unit'],
                    due_date = create_form.cleaned_data['due_date'],
                )
                task.save()
                return redirect('tasks')
        elif 'task_status_submit' in request.POST:
            task_id = request.POST['task_id']
            task = Task.objects.get(pk=task_id)
            task_status_form = TaskStatusForm(request.POST)
            if task_status_form.is_valid():
                choice = task_status_form.cleaned_data['status']
                if choice == 'completed':
                    print("user selected complete")
                    task.status = "Completed"
                    task.save()
                elif choice == 'in_progress':
                    task.status = 'In Progress'
                    task.save()
                elif choice == 'delete':
                    task.delete()
                return redirect('tasks')
    context = {
        'tasks': tasks,
        'search_form': search_form,
        'create_form': create_form,
        'task_status_form': task_status_form,
    }
    return render(request, 'main/tasks.html', context)

@login_required(login_url='login/')
def focus_hub(request):
    user = request.user
     # Get yesterday's date
    yesterday = datetime.now().date() - timedelta(days=1)

    # 1. Yesterday: Calculate the total number of hours for yesterday for the user
    yesterday_sessions = Session.objects.filter(user=user, date=yesterday)
    yesterday_total_hours = yesterday_sessions.aggregate(total_hours=Sum('session_duration_mins'))['total_hours']
    yesterday_total_hours = yesterday_total_hours / 60 if yesterday_total_hours is not None else 0


    # 2. Daily goal: Calculate the number of hours the user has focused today and their goal
    # Retrieve sessions for today
    today_sessions = Session.objects.filter(user=user, date=datetime.now().date())

    # Calculate total hours for today
    today_total_hours = today_sessions.aggregate(total_hours=Sum('session_duration_mins'))
    if today_total_hours['total_hours'] is not None:
        today_total_hours = today_total_hours['total_hours'] / 60
    else:
        today_total_hours = 0

    daily_goal = user.daily_goal
    today_percentage = (today_total_hours/daily_goal)*100

    # 3. Streak: Calculate the streak of consecutive days the user has reached their daily goal
    streak_start_date = datetime.now().date() - timedelta(days=user.streak)
    streak_sessions = Session.objects.filter(user=user, date__gte=streak_start_date, date__lte=datetime.now().date())
    streak_days = len(set([session.date for session in streak_sessions]))
    if yesterday_total_hours == 0:
        streak_days = 0

    # 4. History: Get each day for the past week leading up to today and the number of hours focused
    history_start_date = datetime.now().date() - timedelta(days=6)
    history_data = (
        Session.objects
        .filter(user=user, date__gte=history_start_date, date__lte=datetime.now().date())
        .values('date')
        .annotate(total_hours=Sum('session_duration_mins') / 60)
        .order_by('date')
    )


    session_form = SessionCreateForm()
    settings_form = FocusSettingsForm()
    session_duration = user.focus_period + user.break_duration

    if request.method == 'POST':
        if 'session_submit' in request.POST:
            session_form = SessionCreateForm(request.POST)
            if session_form.is_valid():
                session = Session(
                    user = user,
                    session_duration_mins = session_form.cleaned_data['session_duration_mins'],
                    session_duration_sec = session_form.cleaned_data['session_duration_sec'],
                    goal = user.daily_goal,
                )
                session.save()
                return redirect('focus-hub')

        elif 'focus_settings_submit' in request.POST:
            user_to_update = CustomUser.objects.get(reg_number=user.reg_number)
            settings_form = FocusSettingsForm(request.POST)
            if settings_form.is_valid():
                user_to_update.daily_goal = settings_form.cleaned_data['daily_goal']
                print("Daily goal updated")
                user_to_update.focus_period = settings_form.cleaned_data['focus_period']
                user_to_update.break_duration = settings_form.cleaned_data['break_duration']
                user_to_update.save()
                return redirect('focus-hub')

    # Pass the data to the template
    context = {
        'yesterday_total_hours': yesterday_total_hours,
        'today_total_hours': today_total_hours,
        'today_percentage': today_percentage,
        'daily_goal': daily_goal,
        'streak_days': streak_days,
        'history_data': history_data,
        'session_form': session_form,
        'settings_form': settings_form,
        'session_duration': session_duration,
    }
    return render(request, 'main/focus_hub.html', context)

@login_required(login_url='login/')
def resources(request):
    user = request.user
    units = Unit.objects.filter(course=user.course, year=user.year, semester=user.semester)
    context = {
        'user': user,
        'units': units,
    }
    return render(request, 'main/resources.html', context)

@login_required(login_url='login/')
def unit_details(request, unit_code):
    user = request.user
    units = Unit.objects.filter(course=user.course, year=user.year, semester=user.semester)
    unit = get_object_or_404(Unit, code=unit_code)
    resources = Resource.objects.all()
    context = {
        'unit': unit,
        'units': units,
        'resources': resources,
    }
    return render(request, 'main/unit_details.html', context)

@login_required(login_url='login/')
def performance(request):
    user = request.user
    user_years = list(range(1, user.year + 1))
    user_semesters = list(range(1, user.semester + 1))
    performances = Performance.objects.filter(user=user.reg_number)


    context = {
        'performances': performances,
        'user_years': user_years,
        'user_semesters': user_semesters,
    }
    return render(request, 'main/performance.html', context)
