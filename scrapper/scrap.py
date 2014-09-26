# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

CAMPOS = [u'Concedente',
          u'Beneficiario',
          u'Finalidad',
          u'Importe',
          u'Norma',
          u'Ejercicio',
          u'Importe de ejercicio',
          u'Modo de concesión',
          u'Fecha de informe',
          u'Descripción línea']

def process_soup(soup):
    for p in soup.find_all('p'):
        spans = p.find_all('span')
        if spans:
            # Este 'p' contiene un documento
            doc = str(p)
            doc_extraido = {}

            for campo in CAMPOS:
                pos = doc.find(campo)
                doc = doc[pos:]
                pos = doc.find('</span>') + 7
                end_pos = doc.find('<br/>')
                print "%s: %s" % (campo, doc[pos:end_pos].strip())
            exit(0)

docs_each_iter = 10

for year in xrange(2012,2015):
    ini_doc = 1
    keep_looking = True 
    while keep_looking:
        end_doc = ini_doc + docs_each_iter - 1
        url = "http://mov-brs-01.aragon.es/cgi-bin/CSUB/BRSCGI?CMD=VERLST&BASE=CSUB&docs={0}-{1}&SEC=CSUBPORTAL&SORT=DPTO&OPDEF=%26&SEPARADOR=&DPTO-C=&BENE-C=&EJER-C={2}&MOCO-C=&NORM-C=&FINA-C=".format(ini_doc, end_doc, year)
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        process_soup(soup)
        num_results = len(soup.find_all('p'))/2
        keep_looking = num_results == docs_each_iter 
        ini_doc += docs_each_iter

