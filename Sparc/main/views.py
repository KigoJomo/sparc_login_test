#views.py
# from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone
from .forms import CustomUserCreationForm, TaskSearchForm, TaskCreationForm, TaskStatusForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Course, ImportantDate, Performance, Task, Unit
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

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

# @login_required(login_url='login/')
# def change_task_status(request, task_id):
#     if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         new_status = request.POST.get('new_status')
#         task = get_object_or_404(Task, id=task_id, user=request.user.reg_number)
#         task.status = new_status
#         task.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})

# @login_required(login_url='login/')
# def delete_task(request, task_id):
#     if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         task = get_object_or_404(Task, id=task_id, user=request.user.reg_number)
#         task.delete()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})

@login_required(login_url='login/')
def focus_hub(request):
    return render(request, 'main/focus_hub.html')

@login_required(login_url='login/')
def resources(request):
    return render(request, 'main/resources.html')

@login_required(login_url='login/')
def performance(request):
    return render(request, 'main/performance.html')
