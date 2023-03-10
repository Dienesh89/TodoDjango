from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('todo.urls')),
    path("signup", include('todo.urls')),
    path("login", include('todo.urls')),
    path("handleSignup", include('todo.urls')),
    path("handleLogin", include('todo.urls')),
    path("handleLogout", include('todo.urls')),
    path("addTodo", include('todo.urls')),
    path("deleteTodo/<int:id>", include('todo.urls')),
]
