import sys

from django.shortcuts import render
from django_tables2   import RequestConfig
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import To_do
from .tables import To_doTable
from .forms import Username
from .forms import AddTodo
# Create your views here.

def splash(request):
    username = Username()
    return render(request, 'todo/splash.html', {'username':username})

def index(request):
    if 'username' in request.GET:
        username = request.GET['username']
        request.session['user'] = username
    else:
        username = request.session['user']
    table = To_doTable(To_do.objects.filter(username = request.session['user']).order_by('priority'))
    print table
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    if request.method == 'POST':
        form = AddTodo(request.POST)
        if form.is_valid():
            priority = form.cleaned_data['priority']
            description = form.cleaned_data['description']
            return HttpResponse(request)
    else:
        form = AddTodo()

    context = RequestContext(request, {
        'table':table,
        'username':username,
        'form':form,
    })
    return render(request, 'todo/index.html', context)

def add(request):
    print request.session['user']
    priority = request.POST['priority']
    description = request.POST['description']
    username = request.session['user']
    date = datetime.now()
    t = To_do.objects.create(priority = priority, description = description, username = username)
    return render(request, 'todo/add.html', {
    'priority':priority,
    'description':description,
    'date':date,
    'username':username
    })
