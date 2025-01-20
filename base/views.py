from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login

from base.models import TubeItem

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    class Meta:
        model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = TubeItem
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(url__contains=search_input)

        context["search_input"] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    login_url = "/login"
    model = TubeItem
    context_object_name = "task"
    template_name = "base/task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    login_url = "/login"
    model = TubeItem
    fields = ["url", "description"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    model = TubeItem
    fields = ["url", "description"]
    success_url = reverse_lazy("tasks")


class DeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login"
    model = TubeItem
    context_object_name = "task"
    success_url = reverse_lazy("tasks")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
