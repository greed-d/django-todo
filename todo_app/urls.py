from django.urls import path

from .views import (
    CompleteStatus,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
    UserLoginView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="todo_list"),
    path("create/", TaskCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>/", CompleteStatus.as_view(), name="is_complete"),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
]
