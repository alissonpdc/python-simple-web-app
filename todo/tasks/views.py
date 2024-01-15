from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext


def tasks(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
    else:
        form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks})

def delete(request, id):
    Task.objects.filter(id=id).delete()
    return redirect(reverse('tasks'))

def complete(request, id):
    try:
        task=Task.objects.get(id=id)
        if task.complete:
            task.complete = 0
        else:
            task.complete = 1
        task.save()
        return redirect('/')
    except Exception:
        return HttpResponse("Sorry You are not allowed to access This task ")

def clear(request):
    Task.objects.all().delete()
    return redirect(reverse('tasks'))
