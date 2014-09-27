# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pprint

from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db.models import Sum, Count
from chartit import PivotDataPool, PivotChart
from navegador.models import Concedidas

class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'
    concedidas = Concedidas.objects.filter(ejercicio=2013).values('concedente__name').annotate(importe_total=Sum('importe_ejercicio'), num_conexiones=Count('concedente__name')).order_by('-importe_total')

    def get(self, request, *args, **kwargs):
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.concedidas)
        if request.GET.get('graph', ''):
            concesores_data= \
                PivotDataPool(
                   series= [
                    {'options': {
                     'source': Concedidas.objects.filter(ejercicio=2013),
                     'categories': 'concedente'},
                     'terms': {
                        'importe_total': Sum('importe_ejercicio')
                     }
                    }])

            pivcht = PivotChart(
                datasource = concesores_data, 
                series_options = [
                  {'options': {
                   'type': 'column'},
                   'terms': ['importe_total']}])

            return render_to_response({'chart': pivcht})
        else:    
            return self.render_to_response(self.get_context_data())

    def generate_chart(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EmisoresView, self).get_context_data(**kwargs)
        context['lista_concesores'] = self.concedidas
        return context

class AyudasView(TemplateView):
    template_name = 'navegador/ayudas.html'

class AyudasBeneficiariosView(TemplateView):
    template_name = 'navegador/ayudas_beneficiarios.html'

