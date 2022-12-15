
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path("todo/", include("apps.todo.urls")),
    path("todo_api/", include("apps.api.urls")),
]
