# -*- coding: utf-8 -*-

import django_tables2 as tables
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

class EmisoresTable(tables.Table):
    concedente__name = tables.Column(verbose_name="Concedente")
    num_concesiones = tables.Column(verbose_name="Nº concesiones")
    importe_total = tables.Column(verbose_name="Importe total")

    def render_concedente__name(self, value, record):
        return mark_safe("<a href='%s'>%s</a>" % (reverse('ayudas_concedente', kwargs={'concedente': record['concedente']}), value))

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        attrs = {"class": "table"}


class AyudasTable(tables.Table):
    concedente__name = tables.Column(verbose_name="Concedente")
    beneficiario__name = tables.Column(verbose_name="Beneficiario")
    importe_total = tables.Column(verbose_name="Importe")
    fecha = tables.Column(verbose_name="Fecha informe")

    def render_concedente__name(self, value, record):
        return mark_safe("<a href='%s'>%s</a>" % (reverse('ayudas_concedente', kwargs={'concedente': record['concedente']}), value))

    def render_beneficiario__name(self, value, record):
        return mark_safe("<a href='%s'>%s</a>" % (reverse('ayudas_beneficiario', kwargs={'beneficiario': record['beneficiario']}), value))

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        attrs = {"class": "table"}


class AyudasBeneficiarioTable(tables.Table):
    concedente__name = tables.Column(verbose_name="Concedente")
    importe_total = tables.Column(verbose_name="Importe")
    fecha = tables.Column(verbose_name="Fecha informe")

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        attrs = {"class": "table"}


class AyudasConcedenteTable(tables.Table):
    beneficiario__name = tables.Column(verbose_name="Beneficiario")
    importe_total = tables.Column(verbose_name="Importe")
    fecha = tables.Column(verbose_name="Fecha informe")

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        attrs = {"class": "table"}


class ConvocadasTable(tables.Table):
    titulo = tables.Column(verbose_name="Título")
    fecha = tables.Column(verbose_name="Fecha")

    class Meta:
        attrs = {"class": "table"}


class BeneficiariosTable(tables.Table):
    beneficiario__name = tables.Column(verbose_name="Beneficiario")
    num_concesiones = tables.Column(verbose_name="Nº concesiones")
    importe_total = tables.Column(verbose_name="Importe total")

    def render_beneficiario__name(self, value, record):
        return mark_safe("<a href='%s'>%s</a>" % (reverse('ayudas_beneficiario', kwargs={'beneficiario': record['beneficiario']}), value))

    def render_importe_total(self, value):
        return '%s €' % value

    class Meta:
        attrs = {"class": "table"}
