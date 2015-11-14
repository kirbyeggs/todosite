from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class To_do(models.Model):
    priority = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], default = 1)
    date =  models.DateTimeField(auto_now_add = True)
    description = models.CharField(max_length = 200)
    username = models.CharField(max_length = 20)
