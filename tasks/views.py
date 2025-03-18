from django.shortcuts import render

from tasks.models import Task, Worker, TaskType, Position


def index(request):
    context = {
        "num_tasks": Task.objects.count(),
        "num_workers": Worker.objects.count(),
        "num_task_types": TaskType.objects.count(),
        "num_positions": Position.objects.count(),
    }
    return render(request, "tasks/index.html", context=context)
