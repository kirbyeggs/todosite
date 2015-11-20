import django_tables2 as tables
from .models import To_do

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name
class To_doTable(tables.Table):
    remove = CheckBoxColumnWithName(accessor='pk', verbose_name="Remove")
    class Meta:
        model = To_do
        fields = ('priority','date','description')
        attrs = {'class': 'paleblue'}
