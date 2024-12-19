from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    ListView,
    UpdateView,
    View,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateTodoForm, LoginUser
from .models import TodoTask


class UserLoginView(FormView):
    template_name = "todo_app/login.html"
    form_class = LoginUser
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        print()
        print("---------------------------------------------")
        print(f"username = {username}, password = {password}")
        print("---------------------------------------------")
        print()
        
        user = authenticate(username = username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TodoTask
    template_name = "todo_app/task_create.html"
    form_class = CreateTodoForm
    success_url = reverse_lazy("todo_list")


class TaskListView(LoginRequiredMixin, ListView):
    model = TodoTask
    template_name = "todo_app/task_list.html"
    context_object_name = "todo"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoTask
    form_class = CreateTodoForm
    template_name = "todo_app/task_create.html"
    success_url = reverse_lazy("todo_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoTask
    success_url = reverse_lazy("todo_list")


class CompleteStatus(LoginRequiredMixin, View):
    def post(self, request, pk):
        print(pk)
        task = get_object_or_404(TodoTask, id=pk)
        completed = request.POST.get("completed") == "on"
        task.completed = completed
        task.save()
        return redirect("todo_list")
