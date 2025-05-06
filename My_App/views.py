from .models import Task
from .serializers import Taskserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskListCreateAPIView(APIView):


    def get(self, request):
        tasks = Task.objects.all()
        serializer = Taskserializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Not found'}, status=404)
        serializer = Taskserializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Not found'}, status=404)
        serializer = Taskserializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Not found'}, status=404)
        task.delete()
        return Response(status=204)
