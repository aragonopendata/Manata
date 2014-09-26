from django.conf.urls import patterns, url

from navegador import views

urlpatterns = patterns('',
    url(r'^$', views.emisores, name='emisores'),
    url(r'^ayudas$', views.ayudas, name='ayudas'),
    url(r'^ayudas/beneficiarios$', views.ayudas_beneficiarios, name='ayudas_beneficiarios')
)
