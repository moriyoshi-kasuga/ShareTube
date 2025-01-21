from django.urls import path
from .views import (
    UserTaskList,
    TaskList,
    TaskCreate,
    TaskUpdate,
    DeleteView,
    CustomLoginView,
    RegisterPage,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("register", RegisterPage.as_view(), name="register"),
    path("user", UserTaskList.as_view(), name="user-tubeitems"),
    path("", TaskList.as_view(), name="tubeitems"),
    path("tubeitem-create", TaskCreate.as_view(), name="tubeitem-create"),
    path("tubeitem-update/<int:pk>", TaskUpdate.as_view(), name="tubeitem-update"),
    path("tubeitem-delete/<int:pk>", DeleteView.as_view(), name="tubeitem-delete"),
]
