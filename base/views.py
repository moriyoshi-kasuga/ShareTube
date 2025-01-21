import re

from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from base.models import TubeItem

pattern = r"https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+)"
repatter = re.compile(pattern)

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tubeitems")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tubeitems")

    class Meta:
        model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tubeitems")
        return super(RegisterPage, self).get(*args, **kwargs)


class UserTaskList(LoginRequiredMixin, ListView):
    template_name = "base/user_tubeitem_list.html"
    login_url = "/login"
    model = TubeItem
    context_object_name = "tubeitems"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tubeitems"] = context["tubeitems"].filter(user=self.request.user)

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tubeitems"] = context["tubeitems"].filter(
                url__contains=search_input
            )

        context["search_input"] = search_input

        return context


class TaskList(ListView):
    login_url = "/login"
    model = TubeItem
    context_object_name = "tubeitems"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tubeitems"] = context["tubeitems"].filter(
                url__contains=search_input
            )

        context["search_input"] = search_input

        return context


class CreateForm(forms.ModelForm):
    class Meta:
        model = TubeItem
        fields = ["url", "description"]

    def clean_url(self):
        url = self.cleaned_data["url"]
        result = repatter.search(url)
        if result is None:
            raise forms.ValidationError("Invalid URL")
        return result.group(1)


class TaskCreate(LoginRequiredMixin, CreateView):
    form_class = CreateForm
    login_url = "/login"
    model = TubeItem
    success_url = reverse_lazy("tubeitems")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    model = TubeItem
    fields = ["description"]
    success_url = reverse_lazy("tubeitems")


class DeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login"
    model = TubeItem
    context_object_name = "tubeitem"
    success_url = reverse_lazy("tubeitems")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
