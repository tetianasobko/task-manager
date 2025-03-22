from django.urls import path

from tasks.views import (
    index,
    TasksListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TasksListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
]

app_name = "tasks"
