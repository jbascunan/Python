import pyodbc
import conexion_sql
import requests
import logging
from time import strftime


def getLicitaciones():
    url = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json'
    args = {'ticket': 'BFDF014A-8A7C-4191-A4DE-4C6FA9683992'}
    response = requests.get(url, params=args)
    return response


def insertarBD(response):
    if response.status_code == 200:
        response_json = response.json()  # diccionario
        datos = response_json['Listado']

        try:
            conn = conexion_sql.conectar()
            cursor = conn.cursor()
            for licitacion in datos:
                #valor = valor['CodigoExterno']
                codigo = licitacion.get('CodigoExterno')
                nombre = licitacion.get('Nombre')
                codigoEstado = licitacion.get('CodigoEstado')
                fechaCierre = licitacion.get('FechaCierre')

                cursor.execute("insert into Licitacion(CodigoExterno, Nombre,CodigoEstado,FechaCierre) values (?, ?, ?, ?)",
                               codigo, nombre, codigoEstado, fechaCierre)

            conn.commit()
            conn.close

            logger = logging.getLogger('myapp')
            hdlr = logging.FileHandler(
                strftime("/mislog/mylogfile_%H_%M_%m_%d_%Y.log"))
            formatter = logging.Formatter(
                '%(asctime)s %(levelname)s %(message)s')
            hdlr.setFormatter(formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.WARNING)
        except Exception as ex:
            print('error al insertar datos licitaciones: ', ex)

    else:
        print('error al obtener datos de la api licitaciones')


datosJson = getLicitaciones()
insertarBD(datosJson)
