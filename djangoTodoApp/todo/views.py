from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from .models import Todo
# Create your views here.
def index(request):
    # context = {
    #     "number1" :40,
    #     "number2" :20,
    #     "list" : [1, 4, 7, 8, 9]
    # }
    
    todos = Todo.objects.all()
    return render(request,"index.html",{"todos":todos})


def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(title = title,completed = False)
        newTodo.save()
        return redirect("/")
    

def update(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("/")

def delete(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect("/")
