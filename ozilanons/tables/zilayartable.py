import django_tables2 as tables
from ozilanons.models import ZilData, OkulAksamZaman


class ZilayarTable(tables.Table):
    class Meta:
        model = ZilData
        template_name = 'django_tables2/bootstrap.html'

        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'xzilgun', 'active',)

        exclude = ('published_date', 'id', 'zilgun',)
        order_by = 'zilgun'


class AksamZilayarTable(tables.Table):
    class Meta:
        model = OkulAksamZaman
        template_name = 'django_tables2/bootstrap.html'

        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'xzilgun', 'active',)

        exclude = ('published_date', 'id', 'zilgun',)
        order_by = 'zilgun'