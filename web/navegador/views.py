from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db.models import Sum, Count

from navegador.models import Concedidas

class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'

    def get_context_data(self, **kwargs):
        context = super(EmisoresView, self).get_context_data(**kwargs)
        context['lista_concesores'] = Concedidas.objects.filter(ejercicio=2013).values('concedente__name').annotate(importe_total=Sum('importe_ejercicio'), num_conexiones=Count('concedente__name')).order_by('-importe_total')
        return context

class AyudasView(TemplateView):
    template_name = 'navegador/ayudas.html'

class AyudasBeneficiariosView(TemplateView):
    template_name = 'navegador/ayudas_beneficiarios.html'

