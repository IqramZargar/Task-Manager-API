from django.urls import path
from .views import TaskDetailAPIView, TaskListCreateAPIView

urlpatterns = [
    
    path('My_App/', TaskListCreateAPIView.as_view()),
    path('My_App/<int:pk>/', TaskDetailAPIView.as_view()),
]
