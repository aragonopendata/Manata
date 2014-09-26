# -*- coding: utf-8 -*-

# TODO: Parametrizar años y documentos por iteración

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb

#MYSQL
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = ''
DATABASE = 'subvenciones'

db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE, charset='utf8',
                         use_unicode=True)
cursor = db.cursor()

lista_campos = [u'Concedente',
                u'Beneficiario',
                u'Finalidad',
                u'Importe',
                u'Norma',
                u'Orden',
                u'Ejercicio',
                u'Importe de ejercicio',
                u'Modo de concesión',
                u'Fecha de informe',
                u'Descripción línea']
lista_claves = ['concedente',
                'beneficiario',
                'finalidad',
                'importe',
                'norma',
                'orden',
                'ejercicio',
                'importe_ejercicio',
                'modo_concesion',
                'fecha',
                'descripcion']

# Extracción de los documentos del html
def process_soup(soup):
    for p in soup.find_all('p'):
        spans = p.find_all('span')
        if spans:
            # Este 'p' contiene un documento
            doc = str(p)
            doc_extraido = {}

            for i, campo in enumerate(lista_campos):
                clave = lista_claves[i]
                pos = doc.find(campo)
                if(pos > 0):
                    doc = doc[pos:]
                    pos = doc.find('</span>') + 7
                    end_pos = doc.find('<br/>')
                    doc_extraido[clave] = doc[pos:end_pos].strip()
                else:
                    doc_extraido[clave] = ""
                #print "%s: %s" % (campo, doc_extraido[clave])

            # Formatos para MySQL
            fecha = doc_extraido['fecha']
            fecha_split = fecha.split('/')
            doc_extraido['fecha'] = '20' + fecha_split[2] + '-' + fecha_split[1] + '-' + fecha_split[0]

            doc_extraido['importe'] = doc_extraido['importe'].replace(',','.')
            doc_extraido['importe_ejercicio'] = doc_extraido['importe_ejercicio'].replace(',','.')

            insert = "INSERT INTO subvenciones_concedidas " \
                     "(concedente, beneficiario, finalidad, importe, norma, orden, ejercicio, importe_ejercicio, modo_concesion, fecha, descripcion) " \
                     " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            valores = [doc_extraido.get(clave) for clave in lista_claves]

            try:
                cursor.execute(insert, valores)
            except:
                print "Fallo en:"
                print valores

            db.commit()

docs_each_iter = 1000

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

db.commit()
db.close()
