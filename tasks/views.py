from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .adapters import TaskConsoleAdapter

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks':tasks})


def add_task(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title,description=description)
        return redirect(task_list)
    return render(request,'tasks/add_task.html')


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method=='POST':
        task.title = request.POST.get('title',task.title)
        task.description = request.POST.get('descriptin', task.description)
        task.save()
        return redirect('task_list')
    
    return render(request, 'tasks/update_task.html',{'task':task})


def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method=='POST':
        task.delete()
        return redirect('task_list')
    
    return render (request,'tasks/delete_task.html',{'task':task})