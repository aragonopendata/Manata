from django.conf.urls import patterns, url

from navegador.views import *

urlpatterns = patterns('',
    url(r'^$', EmisoresView.as_view(), name='emisores'),
    url(r'^ayudas$', AyudasView.as_view(), name='ayudas'),
    url(r'^ayudas/beneficiarios$', AyudasBeneficiariosView.as_view(), name='ayudas_beneficiarios')
)
