from django.shortcuts import render, redirect
from .models import Task
from .adapters import TaskConsoleAdapter

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    formatted_tasks =[TaskConsoleAdapter(task).format_for_console() for task in tasks]
    return render(request, 'tasks/task_list.html',{'tasks':formatted_tasks})


def add_task(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title,description=description)
        return redirect(task_list)
    return render(request,'tasks/add_task.html')
