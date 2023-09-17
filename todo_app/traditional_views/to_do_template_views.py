from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from todo_app.models import ToDo
import datetime

# Create your views here.
def index(request):
    if request.method == "GET":
        todo = ToDo.objects.all()
        return render(request,'todo_app/index.html',context={"todo":todo})
    elif request.method == "POST":
        name = request.POST["todo"]
        todo = ToDo.objects.create(title=name,date=datetime.datetime.now().date())
        todo.save()
        return redirect('index')

def delete(request: HttpRequest, todo_id: int) -> HttpResponse:
    todo = get_object_or_404(ToDo, id=todo)
    todo.delete()
    return redirect('index')

def completed(request: HttpRequest, completed_id: int) -> HttpResponse:
    todo = get_object_or_404(ToDo, id=todo)
    todo.is_complete = True
    todo.save()
    return redirect('index')
