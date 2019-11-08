from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def dem():
    return "hello"

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items':all_todo_items})

def addTodoview(request):
    item = TodoItem(content=request.POST.get('content'))
    if item.content.strip() is not "":
        item.save()
    return HttpResponseRedirect('/todo')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo')