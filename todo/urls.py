from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.splash, name= 'splash'),
    url(r'index/', views.index, name='index'),
    url(r'add/', views.add, name='add'),
]
