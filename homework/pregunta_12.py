"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        totals = {}
        for row in csv.reader(file, delimiter="\t"):
            for pair in row[4].split(","):
                key, value = pair.split(":")
                totals[row[0]] = totals.get(row[0], 0) + int(value)

        return dict(sorted(totals.items()))

