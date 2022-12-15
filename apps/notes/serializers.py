from turtle import title
from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'note_title']

class NotesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

