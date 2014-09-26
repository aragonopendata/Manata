#/usr/bin/python

import MySQLdb
import json
import argparse
#from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#MYSQL
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = ''
DATABASE = 'subvenciones'

db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE, charset='utf8',
                         use_unicode=True)
cursor = db.cursor()

parser = argparse.ArgumentParser(description='subvenciones concedidas parser', 
                                 conflict_handler='resolve')
parser.add_argument('json_file')
options = parser.parse_args()

json_data=open(options.json_file)

data = json.load(json_data, encoding="UTF-8")
#print(data)
for convocatoria in data:
    fecha_original = convocatoria["FechaPublicacion"].strip()
    fecha = fecha_original[:4] + '-' + fecha_original[4:6] + '-' + fecha_original[6:]
    seccion = convocatoria["Seccion"].strip()
    subseccion = convocatoria["Subseccion"].strip()
    rango = convocatoria["Rango"].strip()
    emisor = convocatoria["Emisor"].strip()
    titulo = convocatoria["Titulo"].strip()
    texto = convocatoria["Texto"].strip()
    urlpdf = convocatoria["UrlPdf"].strip()

    insert = "INSERT INTO subvenciones_convocadas (fecha, seccion, subseccion, rango, emisor, titulo, texto, urlpdf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert,
                   (fecha, seccion, subseccion, rango, emisor, titulo, texto, urlpdf)
                  )
    db.commit()
db.close()
json_data.close()
