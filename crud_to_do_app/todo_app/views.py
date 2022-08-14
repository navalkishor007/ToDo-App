from django.shortcuts import render, redirect
from datetime import datetime
from .models import TodoData

# Create your views here.

def home_page(request):
    data = TodoData.objects.all()
    if request.method == 'POST':
        data = TodoData()
        task = request.POST['to_do_task']
        time = request.POST['to_do_time']
        data.task_to_do = task
        data.by_when_to_do = time
        data.save()
        print(task, 'and time is ', time)
        return redirect('/')
    return render(request, 'todo_app/index.html', {'data':data})

def to_do_task(request):
    return render(request, 'todo_app/todo_form.html')

def task_delete(request,id):
    data = TodoData.objects.get(id=id)
    data.delete()
    return redirect('/')

def task_update(request,id):
    data = TodoData.objects.all()
    vals = TodoData.objects.get(id=id)
    start_date = vals.by_when_to_do
    date = start_date.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        task = request.POST['to_do_task']
        time = request.POST['to_do_time']
        vals.task_to_do = task
        vals.by_when_to_do = time
        vals.save()
        return redirect('/')
    return render(request, 'todo_app/index.html', {'vals':vals, 'data':data, 'date':date})
