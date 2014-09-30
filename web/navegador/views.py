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

# FIXME
from navegador.models import *
from navegador.tables import *


class Index(TemplateView):
    template_name = 'navegador/index.html'

class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'

    def get_chart(self):
        concesores_data= \
            PivotDataPool(
                series= [
                {'options': {
                    'source': Concedidas.objects.all().values('concedente__name', 'importe_ejercicio'),
                    'categories': 'concedente__name'},
                    'terms': {
                    'importe_total': Sum('importe_ejercicio'),
                    }
                }])

        pivcht = PivotChart(
            datasource = concesores_data,
            series_options = [
                {'options': {
                'type': 'bar'},
                'terms': ['importe_total']}],
            chart_options = {
                'title': {
                   'text': 'Importe total de subvenciones concedidas'},
            }
        )

        return pivcht

    def get_context_data(self, **kwargs):
        context = super(EmisoresView, self).get_context_data(**kwargs)
        lista_concesores = Concedidas.objects.all().values('concedente__name', 'concedente').annotate(importe_total=Sum('importe_ejercicio'), num_concesiones=Count('concedente__name')).order_by('-importe_total')
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
        concesiones = Concedidas.objects.all().values('concedente__name', 'beneficiario__name', 'fecha', 'concedente', 'beneficiario').annotate(importe_total=Sum('importe_ejercicio')).order_by('-fecha')
        table = AyudasTable(concesiones)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table

        return context


class AyudasBeneficiarioView(TemplateView):
    template_name = 'navegador/ayudas_beneficiario.html'

    def get_context_data(self, **kwargs):
        context = super(AyudasBeneficiarioView, self).get_context_data(**kwargs)
        beneficiario = kwargs.get('beneficiario')
        concesiones = Concedidas.objects.filter(beneficiario=beneficiario).order_by('-fecha')
        context['beneficiario'] = Beneficiarios.objects.get(id=beneficiario)
        table = AyudasBeneficiarioTable(concesiones)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table

        return context


class AyudasConcedenteView(TemplateView):
    template_name = 'navegador/ayudas_concedente.html'

    def get_context_data(self, **kwargs):
        context = super(AyudasConcedenteView, self).get_context_data(**kwargs)
        concedente = kwargs.get('concedente')
        concesiones = Concedidas.objects.filter(concedente=concedente).order_by('-fecha')
        context['concedente'] = Concedentes.objects.get(id=concedente)
        table = AyudasConcedenteTable(concesiones)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table

        return context


class BeneficiariosView(TemplateView):
    template_name = 'navegador/beneficiarios.html'

    def get_context_data(self, **kwargs):
        context = super(BeneficiariosView, self).get_context_data(**kwargs)
        lista_beneficiarios = Concedidas.objects.all().values('beneficiario__name', 'beneficiario').annotate(importe_total=Sum('importe_ejercicio'), num_concesiones=Count('concedente__name')).order_by('-importe_total')
        table = BeneficiariosTable(lista_beneficiarios)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        return context

class ConvocadasView(TemplateView):
    template_name = 'navegador/convocadas.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocadasView, self).get_context_data(**kwargs)
        emisor = kwargs.get('emisor')
        lista_convocadas = Convocadas.objects.values('titulo', 'fecha', 'urlpdf').order_by('-fecha')
        table = ConvocadasTable(lista_convocadas)
        RequestConfig(self.request, paginate={"per_page": 25}).configure(table)
        context['table'] = table
        return context

class SubvencionView(TemplateView):
    template_name = 'navegador/subvencion.html'

    def get_context_data(self, **kwargs):
        context = super(SubvencionView, self).get_context_data(**kwargs)
        subvencion_id = kwargs.get('subvencion')
        subvencion = Concedidas.objects.get(id=subvencion_id)
        context['subvencion'] = subvencion
        return context
