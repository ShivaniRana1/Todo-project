from django.urls import path
from .to_do_views import ToDoDetailAPIView, ToDoListCreateAPIView

urlpatterns = [
    path('todos/', ToDoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoDetailAPIView.as_view(), name='todo-detail'),
    path('todos/<int:pk>/complete/', ToDoDetailAPIView.as_view(), name='todo-complete'),
]
