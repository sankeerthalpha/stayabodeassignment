from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Deleted
from django.http import HttpResponse


def status_report(request):
    todo_listing = []
    for todo_list in List.objects.all().order_by("-id"):
        todo_dict = {}
        todo_dict['list_object'] = todo_list
        todo_dict['item_count'] = todo_list.item_set.count()
        todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()
        if todo_dict['item_count']:
            todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)
        else:
            todo_dict['percent_complete'] = 0
        todo_listing.append(todo_dict)
    return render(request, 'todolist/status_report.html', {'todo_listing': todo_listing})


def addForm(request):
    return render(request, "todolist/addForm.html", {})


def addTask(request):
    task = request.POST.get('addtask')
    try:
        new_task = List(title=task)
        new_task.save()
    except Exception as e:
        return HttpResponse("Unable to save task. Task title might be duplicate")
    return redirect('/todolist/')


def updateForm(request, task_id):
    task = get_object_or_404(List, pk=task_id)
    return render(request, 'todolist/updateForm.html', {'task': task})


def updateTask(request):
    task_id = request.POST.get('taskid')
    updated_task = request.POST.get('updatetask')
    try:
        task = List.objects.get(pk=task_id)
        task.title = updated_task
        task.save()
    except Exception as e:
        return HttpResponse("Unable to save task. Task title might be duplicate")
    return redirect('/todolist/')


def deleteTask(request, task_id):
    try:
        task = List.objects.get(pk=task_id)
        title = task.title
        task.delete()
        deleted_task = Deleted(title=title)
        deleted_task.save()
    except Exception as e:
        return HttpResponse("Error while deleting the task")
    return redirect('/todolist/')


