from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import ToDo
from ..serializers.to_do_serializer import ToDoSerializer

class ToDoListCreateAPIView(generics.ListCreateAPIView):
    """
    This lists all the todo activities.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This provides retrive, update and delete methods for the todo activity.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    @action(detail=True, methods=['post'])
    def complete_todo(self, request: Request, *args, **kwargs) -> Response:
        """
        This marks the activty as completed.

        :param request: The rest framework request object.
        :returns: The rest framework response.
        """
        todo = self.get_object()
        todo.is_complete = True
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)
