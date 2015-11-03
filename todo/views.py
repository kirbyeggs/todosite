from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import To_do

# Create your views here.
def index(request):
    todo_list = To_do.objects.order_by('priority')
    template = loader.get_template('todo/index.html')
    context = RequestContext(request, {
        'todo_list':todo_list,
    })
    return HttpResponse(template.render(context))