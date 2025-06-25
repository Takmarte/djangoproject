from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Todos
from .forms import ListForm
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todos.objects.all()
            return render(request,"todo_app/index.html",{'todo_list':todo_list})
    else:
        todo_list = Todos.objects.all()
        return render(request,"todo_app/index.html",{'todo_list':todo_list})

def about(request):
    return render(request,"todo_app/about.html")

def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            todo = form.save(commit=False)

            
            if todo.finished:
                todo.finished_date = datetime.now()

            todo.save()
            return redirect("index")  
    else:
        form = ListForm()

    return render(request, "todo_app/create.html", {'form': form})

def delete(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")

def yes_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = False
    todo.finished_date = None
    todo.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def no_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = True  
    todo.finished_date = datetime.now()
    todo.save()
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def update(request, Todos_id):
    todo_item = get_object_or_404(Todos, pk=Todos_id)

    if request.method == "POST":
        form = ListForm(request.POST, instance=todo_item)
        if form.is_valid():
            todo = form.save(commit=False)

            if todo.finished and not todo.finished_date:
                todo.finished_date = datetime.now()         
            elif not todo.finished:
                todo.finished_date = None

            todo.save()
            return redirect("index")
    else:
        form = ListForm(instance=todo_item)

    return render(request, "todo_app/update.html", {'form': form})
  

def description(request, id):
    todo = get_object_or_404(Todos, id=id)  # sadece o id'deki görevi çeker
    return render(request, 'todo_app/description.html', {'todo': todo})