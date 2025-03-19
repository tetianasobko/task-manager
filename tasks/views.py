from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Worker, TaskType, Position


def index(request):
    pending_tasks = (
        Task.objects.filter(is_completed=False)
        .order_by('-priority', 'deadline')
    )

    context = {
        "num_tasks": Task.objects.count(),
        "num_workers": Worker.objects.count(),
        "num_task_types": TaskType.objects.count(),
        "num_positions": Position.objects.count(),
        "pending_tasks": pending_tasks,
    }
    return render(request, "tasks/index.html", context=context)


class TasksListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
