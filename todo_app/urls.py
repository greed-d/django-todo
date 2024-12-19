from django.urls import path

from .views import (
    CompleteStatus,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskCreateView.as_view(), name="todo_create"),
    path("list/", TaskListView.as_view(), name="todo_list"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>/", CompleteStatus.as_view(), name="is_complete"),
]
