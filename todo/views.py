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
from .forms import SearchTodo
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
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    search = SearchTodo()

    if request.method == 'POST':
        add = AddTodo(request.POST)
        if add.is_valid():
            priority = add.cleaned_data['priority']
            description = add.cleaned_data['description']
            return HttpResponse(request)
    else:
        add = AddTodo()

    context = RequestContext(request, {
        'table':table,
        'username':username,
        'add':add,
        'search':search
    })
    return render(request, 'todo/index.html', context)

def add(request):
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

def remove(request):
    if request.method == 'POST':
        pks = request.POST.getlist('remove')
        To_do.objects.filter(pk__in = pks).delete()
        num = len(pks)
    else:
        pass
    return render(request, 'todo/remove.html', {
    'num':num,
    })

def search(request):
    entry = request.GET['description']
    search = SearchTodo()
    username = request.session['user']
    table = To_doTable(To_do.objects.filter(username =  request.session['user'], description__contains = entry))
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    return render(request, 'todo/search.html', {
    'table':table,
    'username':username,
    'search':search,
    'entry':entry,
    })
