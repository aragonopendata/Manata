# -*- coding: utf-8 -*-

import django_tables2 as tables
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

class EmisoresTable(tables.Table):
    concedente__name = tables.Column(verbose_name="Emisores")
    num_concesiones = tables.Column(verbose_name="Nº concesiones")
    importe_total = tables.Column(verbose_name="Importe total")

    def render_concedente__name(self, value, record):
        return mark_safe("<a href='%s'>%s</a>" % (reverse('ayudas', kwargs={'emisor': record['concedente']}), value))

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        #attrs = {"class": "paleblue"}
        attrs = {"class": "table"}
