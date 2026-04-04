from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Todo

def task_list(request):
    task = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        tittle = request.POST.get('tittle', '').strip()
        description = request.POST.get('description', '').strip()

        if tittle:
            Todo.objects.create(
                tittle=tittle,
                description=description,
                date=timezone.now().date(),
                 
              
            )
            return redirect(reverse('todo:task_list'))

        error = 'Tittle cannot be empty'
        return render(request, 'todo/task_form.html', {'errors': error})

    return render(request, 'todo/task_form.html')


def task_update(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        tittle = request.POST.get('tittle', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'

        if tittle:
            task.tittle = tittle
            task.description = description
            task.completed = completed
            task.save()
            return redirect(reverse('todo:task_list'))

        return render(request, 'todo/task_form.html', {
            'task': task,
            'error': 'Tittle cannot be empty'
        })

    return render(request, 'todo/task_form.html', {'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))

    return render(request, 'todo/task_confirm_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return redirect(reverse('todo:task_list'))

    return redirect(reverse('todo:task_list'))