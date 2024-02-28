# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Unit, Task, Performance, Resource, ImportantDate

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "reg_number", "course", "year", "semester",)
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
    list_display = ("code", "name", "course",)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "unit", "status",)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("user", "unit", "score",)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "unit",)

class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date",)

# Register your models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ImportantDate, ImportantDateAdmin)
