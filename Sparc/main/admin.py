# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Unit, Task, Performance, Resource, ImportantDate, Session

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "reg_number", "course_name", "year", "semester",)

    def course_name(self, obj):
        return obj.course.name

    list_filter = ("email", "reg_number", "course", "year", "semester", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "reg_number", "password")}),
        ("Personal Info", {"fields": ("course", "year", "semester")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "reg_number", "course", "year", "semester", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions")
        }),
    )
    search_fields = ("email", "reg_number")
    ordering = ("email",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name",)

class UnitAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "display_course_name",)

    def display_course_name(self, obj):
        return obj.course.name

    display_course_name.short_description = 'Course Name'


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "unit_name", "created_at", "due_date", "status",)

    def unit_name(self, obj):
        return obj.unit.name

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("user", "unit_name", "score", "grade",)

    def unit_name(self, obj):
        return obj.unit.name

class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "unit",)

class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date",)

class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "session_duration_mins", "session_duration_sec", "goal", "date",)

# Register your models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ImportantDate, ImportantDateAdmin)
admin.site.register(Session, SessionAdmin)
