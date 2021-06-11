from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Todo
from .forms import *


def index(request):

    t = Todo.objects.all()

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'task/list.html', {'t':t,'form':form})

def updatetask(request, pk):
    task = Todo.objects.get(id = pk)
    form = TodoForm(instance=task)
    context = {'form':form}

    if request.method == "POST":
        form = TodoForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'task/update_task.html',context)

def delete(request, pk):
    
    item = Todo.objects.get(id = pk)  
    context = {'item':item}
    if request.method == "POST":
        item.delete()
        return redirect("/")
    # return HttpResponse("delete")
    return render(request, 'task/delete.html', context)