from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactsList.as_view()),
    path('<int:pk>/', views.ContactsDetail.as_view()),
    path('togglefave/<int:pk>/', views.ToggleFaveComplete.as_view()),
]

# urlpatterns += [
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
