from django.conf.urls import patterns, url

from navegador import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^emisor$', views.emisor, name='emisor'),
    url(r'^emisor/ayuda$', views.ayuda, name='ayuda')
)
