from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db.models import Sum, Count

from django_tables2 import RequestConfig

from navegador.models import Concedidas
from navegador.tables import EmisoresTable


class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'

    def get_context_data(self, **kwargs):
        context = super(EmisoresView, self).get_context_data(**kwargs)
        lista_concesores = Concedidas.objects.filter(ejercicio=2013).values('concedente__name').annotate(importe_total=Sum('importe_ejercicio'), num_concesiones=Count('concedente__name')).order_by('-importe_total')
        table = EmisoresTable(lista_concesores)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        return context


class AyudasView(TemplateView):
    template_name = 'navegador/ayudas.html'


class AyudasBeneficiariosView(TemplateView):
    template_name = 'navegador/ayudas_beneficiarios.html'

