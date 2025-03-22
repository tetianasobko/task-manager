from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm, WorkerCreateForm, WorkerPositionUpdateForm
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


class TaskTypesListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"


class TasksListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "tasks/worker_list.html"


class WorkerDetailView(generic.DetailView):
    model = get_user_model()
    template_name = "tasks/worker_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["completed_tasks"] = self.object.tasks.filter(
            is_completed=True).count()
        return context


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    template_name = "tasks/worker_create_form.html"
    success_url = reverse_lazy("tasks:worker-list")


class WorkerPositionUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerPositionUpdateForm
    template_name = "tasks/worker_update_form.html"

    def get_success_url(self):
        return reverse_lazy(
            'tasks:worker-detail', kwargs={'pk': self.object.pk}
        )


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")
