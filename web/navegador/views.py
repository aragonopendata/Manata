from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse

class EmisoresView(TemplateView):
    template_name = 'navegador/emisores.html'

class AyudasView(TemplateView):
    template_name = 'navegador/ayudas.html'

class AyudasBeneficiariosView(TemplateView):
    template_name = 'navegador/ayudas_beneficiarios.html'

