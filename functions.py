'''
Funciones [Python]
---------------------------
Autor: Emmanuel Oscar Torres Molina
Version: 1.1
Descripción:
Programa creado para utilizar en el programa
"ejercicios_practica.py"
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import sqlite3
import csv
import os

db = 'tabla_del_cinco.db'
nombre_archivo = 'tabla_del_cinco.csv'


def create_schema():
    path_script = os.path.realpath(os.path.dirname(__file__))
    path_schema = os.path.join(path_script, 'schema.sql')

    conn = sqlite3.connect(db)

    conn.executescript(open(path_schema, 'r').read())

    conn.commit()
    conn.close()


def fill(valor):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(
        """ INSERT INTO tabla_del_cinco (result)
            VALUES (?);""", (valor,))

    conn.commit()
    conn.close()


def show():
    conn = sqlite3.connect(db)
    c = conn.cursor()

    query = """ SELECT *
            FROM tabla_del_cinco;
            """
    
    c.execute(query)

    query_result = c.fetchall()

    conn.close()

    return query_result 



def write_header_csv():
    path_script = os.path.realpath(os.path.dirname(__file__))
    path_archivo_csv = os.path.join(path_script, nombre_archivo)

    file_exists = os.path.isfile(path_archivo_csv)

    if not file_exists:
        header = ['numero', 'resultado']

        with open(path_archivo_csv, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()


def cant_rows ():
    path_script = os.path.realpath(os.path.dirname(__file__))
    path_archivo_csv = os.path.join(path_script, nombre_archivo)

    with open(path_archivo_csv, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    return len(data)



def writer_csv(valor):
    path_script = os.path.realpath(os.path.dirname(__file__))
    path_archivo_csv = os.path.join(path_script, nombre_archivo)

    write_header_csv()

    header = ['numero', 'resultado']

    row = {}
    
    with open(path_archivo_csv, 'a', newline='') as csvfile:
        row = {header[0]: cant_rows() + 1, header[1]: valor}
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writerow(row)


def read_csv():
    path_script = os.path.realpath(os.path.dirname(__file__))
    path_archivo_csv = os.path.join(path_script, nombre_archivo)

    with open(path_archivo_csv, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    return data
