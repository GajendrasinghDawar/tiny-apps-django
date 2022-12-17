from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.NotesList.as_view()),
    path('<int:pk>/', views.NotesDetail.as_view())
]


# urlpatterns = [
#     path('', views.NotesList.as_view()),
#     path('<int:pk>/', views.NotesDetail.as_view()),
# ]
