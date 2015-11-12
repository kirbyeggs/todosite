from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import To_do
from .forms import Username
# Create your views here.
def index(request):
    username = request.GET['username']
    todo_list = (To_do.objects.filter(username = username)).order_by('priority')
    template = loader.get_template('todo/index.html')
    context = RequestContext(request, {
        'todo_list':todo_list,
        'username':username
    })
    return HttpResponse(template.render(context))

def splash(request):
    username = Username()
    return render(request, 'todo/splash.html', {'username':username})
