from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import To_do
from .forms import Username
from .forms import AddTodo
# Create your views here.

def splash(request):
    username = Username()
    return render(request, 'todo/splash.html', {'username':username})

def index(request):
    username = request.GET['username']
    request.session['user'] = username
    todo_list = (To_do.objects.filter(username = username)).order_by('priority')
    template = loader.get_template('todo/index.html')

    if request.method == 'POST':
        form = AddTodo(request.POST)
        if form.is_valid():
            priority = form.cleaned_data['priority']
            description = form.cleaned_data['description']
            username = username
            return HttpResponseRedirect(reverse('add'))
    else:
        form = AddTodo()

    context = RequestContext(request, {
        'todo_list':todo_list,
        'username':username,
        'form':form,
    })
    return HttpResponse(template.render(context))

def add(request):
    priority = request.POST['priority']
    description = request.POST['description']
    username = request.session['user']
    t = To_do.objects.create(priority = priority, description = description, username = username)
    return render(request, 'todo/add.html', {
    'priority':priority,
    'description':description,
    'date':date,
    'username':username
    })
