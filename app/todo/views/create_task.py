from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo, STATUS_OF_TASK


def add_view(request):
    if request.method == 'GET':
        context = {
            'status_list': STATUS_OF_TASK
        }
        return render(request, 'create_task.html', context=context)

    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'lead_at': request.POST.get('lead_at')
    }
    task = Todo.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)

def detail_view(request, pk):
    todo_task = get_object_or_404(Todo, pk=pk)
    return render(request, 'task.html', context={'todo_task': todo_task})
