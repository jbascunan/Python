import pyodbc
import conexion_sql
import requests


def getLicitaciones():
    url = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json'
    args = {'ticket': 'BFDF014A-8A7C-4191-A4DE-4C6FA9683992'}
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        response_json = response.json()  # diccionario
        origin = response_json['Listado']
        # print(origin)

        for valor in origin:
            valor = valor['CodigoExterno']
            print(valor)


conn = conexion_sql.conectar()

cursor = conn.cursor()

cursor.execute("select * from clientes")
rows = cursor.fetchall()
for row in rows:
    print(row.cli_nombre)

conn.close

getLicitaciones()
