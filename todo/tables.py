import django_tables2 as tables
from .models import To_do

class To_doTable(tables.Table):
    class Meta:
        model = To_do
        fields = ('priority','date','description')
        attrs = {'class': 'paleblue'}
