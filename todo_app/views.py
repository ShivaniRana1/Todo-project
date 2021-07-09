from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from todo_app.models import ToDo
import datetime

# Create your views here.
def index(request):
    if request.method == "GET":
        todo = ToDo.objects.all()
        print("***********************")
        print(todo)
        return render(request,'todo_app/index.html',context={"todo":todo})

        
    elif request.method == "POST":
        name = request.POST["todo"]
        todo = ToDo.objects.create(title=name,date=datetime.datetime.now().date())
        todo.save()
        return redirect('index')

def delete(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def completed(request,completed_id):
    todo = ToDo.objects.get(id=completed_id)
    todo.is_complete = True
    todo.save()
    return redirect('index')

