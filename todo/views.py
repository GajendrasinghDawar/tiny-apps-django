from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from .models import Entry

def demologin(request, **kargs):
    from django.conf import settings
    user = authenticate(username=settings.TEST_USER,
                        password=settings.TEST_USER_PASSWORD)

    if user is not None:
        login(request, user)
        return redirect('entry-list')
    else:
        return redirect('login')


class LockedView(LoginRequiredMixin):
    login_url = "login/"


class EntryListView(LockedView, ListView):
    model = Entry
    # queryset = Entry.objects.all().order_by("-date_created")
    queryset = Entry.objects.all()


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    template_name_suffix = '_create_form'
    fields = ["title", 'note', 'user', 'completed']
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    template_name_suffix = '_create_form'
    fields = ["title", 'note', 'user', 'completed']
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )


class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
