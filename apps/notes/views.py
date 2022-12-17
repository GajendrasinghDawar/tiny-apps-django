from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Notes
from .serializers import NotesSerializer, NotesDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import generics


class NotesList(generics.ListAPIView):
    queryset = Notes.objects.all()

    serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesDetailSerializer
