from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index , name="index"),
    path("signup", views.signUp , name="signup"),
    path("login", views.login , name="login"),
    path("handleSignup", views.handleSignup , name="handleSignup"),
    path("handleLogin", views.handleLogin , name="handleLogin"),
    path("handleLogout", views.handleLogout , name="handleLogout"),
    path("addTodo", views.addTodo , name="addTodo"),
    path("deleteTodo/<int:id>", views.deleteTodo , name="deleteTodo"),

]
