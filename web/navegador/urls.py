from django.conf.urls import patterns, url

from navegador.views import *

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^emisores/$', EmisoresView.as_view(), name='emisores'),
    url(r'^ayudas/$', AyudasView.as_view(), name='ayudas'),
    url(r'^ayudas/beneficiario/(?P<beneficiario>\d+)/$', AyudasBeneficiarioView.as_view(), name='ayudas_beneficiario'),
    url(r'^ayudas/concedente/(?P<concedente>\d+)/$', AyudasConcedenteView.as_view(), name='ayudas_concedente'),
    url(r'^beneficiarios/$', BeneficiariosView.as_view(), name='beneficiarios'),
    url(r'^convocadas/$', ConvocadasView.as_view(), name='convocadas'),
    url(r'^subvencion/(?P<subvencion>\d+)/$$', SubvencionView.as_view(), name='subvencion'),
)
