from rest_framework import serializers
from apps.todo.models import Entry


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()  # test it
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Entry
        fields = ['id', 'title', 'note', 'created_at', 'completed', ]


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id']
        read_only_fields = ['title', 'note', 'created_at', 'completed']
