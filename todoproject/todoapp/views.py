from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDetailstview(DetailView):
        model = Task
        template_name = 'details.html'
        context_object_name = 'task'


class TaskUpdatetview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        taskname = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=taskname, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task': task1})

# def details(request):
#   task = Task.objects.all()
#   return render(request,'details.html',{'task': task})#

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    f = Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'todoform': f, 'task': task})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cdvhome') #name='cdvhome'

