from django.urls import path
from todo_app.traditional_views import to_do_template_views

urlpatterns = [
    path('', to_do_template_views.index,name='index'),
    path('delete/<int:todo_id>', to_do_template_views.delete,name='delete'),
    path('completed/<int:completed_id>', to_do_template_views.completed,name='completed'),
]