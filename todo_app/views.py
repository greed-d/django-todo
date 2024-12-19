from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from .forms import CreateTodoForm
from .models import TodoTask


class TaskCreateView(CreateView):
    model = TodoTask
    template_name = "todo_app/task_create.html"
    form_class = CreateTodoForm
    success_url = reverse_lazy("todo_list")


class TaskListView(ListView):
    model = TodoTask
    template_name = "todo_app/task_list.html"
    context_object_name = "todo"


class TaskUpdateView(UpdateView):
    model = TodoTask
    form_class = CreateTodoForm
    template_name = "todo_app/task_create.html"
    success_url = reverse_lazy("todo_list")


class TaskDeleteView(DeleteView):
    model = TodoTask
    success_url = reverse_lazy("todo_list")


class CompleteStatus(View):
    def post(self, request, pk):
        print(pk)
        task = get_object_or_404(TodoTask, id=pk)
        completed = request.POST.get("completed") == "on"
        task.completed = completed
        task.save()
        return redirect("todo_list")
