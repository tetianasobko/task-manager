from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from tasks.forms import (
    TaskForm,
    WorkerCreateForm,
    WorkerPositionUpdateForm,
    TaskSearchForm,
    WorkerSearchForm,
    PositionSearchForm
)
from tasks.models import Task, Worker, TaskType, Position


class Index(LoginRequiredMixin, TemplateView):
    template_name = "tasks/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["num_tasks"] = Task.objects.count()
        context["num_workers"] = Worker.objects.count()
        context["num_task_types"] = TaskType.objects.count()
        context["num_positions"] = Position.objects.count()
        context["pending_tasks"] = Task.objects.filter(
            is_completed=False
        ).order_by("deadline", "-priority")[:7]
        return context


class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(TaskTypesListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypesCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-types-list")


class TaskTypesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-types-list")


class TaskTypesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "tasks/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-types-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "tasks/position_list.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_form.html"
    success_url = reverse_lazy("tasks:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_form.html"
    success_url = reverse_lazy("tasks:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "tasks/position_confirm_delete.html"
    success_url = reverse_lazy("tasks:position-list")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "tasks/worker_list.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"])
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "tasks/worker_detail.html"

    def get_context_data(self, **kwargs):
        context = super(WorkerDetailView, self).get_context_data(**kwargs)
        context["completed_tasks"] = self.object.tasks.filter(
            is_completed=True).count()
        return context


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    template_name = "tasks/worker_create_form.html"
    success_url = reverse_lazy("tasks:worker-list")


class WorkerPositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerPositionUpdateForm
    template_name = "tasks/worker_update_form.html"

    def get_success_url(self):
        return reverse_lazy(
            'tasks:worker-detail', kwargs={'pk': self.object.pk}
        )


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")


@login_required
def toggle_complete_to_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:task-detail", args=[pk]))
