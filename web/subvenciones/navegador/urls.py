from django.conf.urls import patterns, url

from navegador import views

urlpatterns = patterns('',
#    url(r'^$', views.Main.as_view(), name='main')
    url(r'^$', views.main, name='main')
)