from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task_type', 'title', 'description', 'is_done', 'created_at')
        read_only_fields = ('id', 'created_at')
