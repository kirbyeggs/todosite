from django.db import models

# Create your models here.
class To_do(models.Model):
    priority = models.IntegerField(default = 1)
    date =  models.DateTimeField('date inputted')
    description = models.CharField(max_length = 200)
    username = models.CharField(max_length = 20)
