from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Task, Worker, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "position")
    search_fields = ("first_name", "last_name")
    list_filter = ("position",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name", "description", "deadline", "is_completed", "priority",
        "task_type"
    )
    search_fields = ("name", "description")
    list_filter = ("is_completed", "priority", "task_type")


admin.site.register(TaskType)
admin.site.register(Position)
