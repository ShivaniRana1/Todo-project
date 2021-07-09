from django.urls import path
from todo_app import views

urlpatterns = [
    
    path('', views.index,name='index'),
    path('delete/<int:todo_id>', views.delete,name='delete'),
    path('completed/<int:completed_id>', views.completed,name='completed'),
]