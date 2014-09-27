# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db.models import Sum, Count
from chartit import PivotDataPool, PivotChart

from django_tables2 import RequestConfig

from navegador.models import Concedidas, Convocadas, Concedentes
from navegador.tables import AyudasBeneficiariosTable, AyudasTable, EmisoresTable, ConvocadasTable


class Index(TemplateView):
    template_name = 'navegador/index.html'

class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'

    def get_chart(self):
        concesores_data= \
            PivotDataPool(
                series= [
                {'options': {
                    'source': Concedidas.objects.filter(ejercicio=2013).values('concedente__name', 'importe_ejercicio'),
                    'categories': 'concedente__name'},
                    'terms': {
                    'importe_total': Sum('importe_ejercicio'),
                    }
                }])

        pivcht = PivotChart(
            datasource = concesores_data,
            series_options = [
                {'options': {
                'type': 'column'},
                'terms': ['importe_total']}],
            chart_options = {})

        return pivcht

    def generate_chart(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EmisoresView, self).get_context_data(**kwargs)
        lista_concesores = Concedidas.objects.filter(ejercicio=2013).values('concedente__name', 'concedente').annotate(importe_total=Sum('importe_ejercicio'), num_concesiones=Count('concedente__name')).order_by('-importe_total')
        table = EmisoresTable(lista_concesores)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        context['chart'] = self.get_chart()
        return context


class AyudasView(TemplateView):
    template_name = 'navegador/ayudas.html'

    def get_context_data(self, **kwargs):
        context = super(AyudasView, self).get_context_data(**kwargs)
        emisor = kwargs.get('emisor')
        if emisor:
            concesiones = Concedidas.objects.filter(concedente=emisor)
            context['concedente'] = Concedentes.objects.get(id=emisor)
        else:
            concesiones = Concedidas.objects.all()
        concesiones = concesiones.values('beneficiario__name', 'fecha').annotate(importe_total=Sum('importe_ejercicio')).order_by('-fecha')
        table = AyudasTable(concesiones)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        # TODO: Chart???

        return context


class AyudasBeneficiariosView(TemplateView):
    template_name = 'navegador/ayudas_beneficiarios.html'

    def get_context_data(self, **kwargs):
        context = super(AyudasBeneficiariosView, self).get_context_data(**kwargs)
        # origen_subvencion = kwargs
        lista_beneficiarios = Concedidas.objects.filter(ejercicio=2013).values('beneficiario__name', 'descripcion').annotate(importe_total=Sum('importe_ejercicio'), num_concesiones=Count('beneficiario__name')).order_by('beneficiario__name', '-importe_total')
        table = AyudasBeneficiariosTable(lista_beneficiarios)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        return context

class ConvocadasView(TemplateView):
    template_name = 'navegador/convocadas.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocadasView, self).get_context_data(**kwargs)
        emisor = kwargs.get('emisor')
        lista_convocadas = Convocadas.objects.values('titulo', 'fecha').order_by('-fecha')
        table = ConvocadasTable(lista_convocadas)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        return context


