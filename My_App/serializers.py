from rest_framework import serializers
from .models import Task


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = '__all__'