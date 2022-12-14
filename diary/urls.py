from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

# todo
urlpatterns += [
    path("todo/", include("apps.todo.urls")),
    path("todo_api/", include("apps.api.urls")),
]


# moview review
urlpatterns += [
    path('movie_review/', include('apps.movie.urls')),
    path('news/', include('apps.news.urls')),
    path('accounts/', include('apps.accounts.urls')),
]


# myPortFolio api app
urlpatterns += [
    path('myportfolio_api/', include('apps.notes.urls')),
]


# contacts book
urlpatterns += [
    path('contacts_book_api/', include('apps.contacts_book.urls')),
]

# moview review
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# tiny-apps-django.diary.settings.py
