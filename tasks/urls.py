from django.urls import path

from tasks.views import (
    index,
    TaskTypesListView,
    TaskTypesCreateView,
    TaskTypesUpdateView,
    TaskTypesDeleteView,
    TasksListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerPositionUpdateView,
    WorkerDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("task-types/", TaskTypesListView.as_view(), name="task-types-list"),
    path("task-types/create/", TaskTypesCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/update", TaskTypesUpdateView.as_view(), name="task-type-update"),
    path("task-types/<int:pk>/delete", TaskTypesDeleteView.as_view(), name="task-type-delete"),
    path("tasks/", TasksListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
         name="task-delete"
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerPositionUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
]

app_name = "tasks"
