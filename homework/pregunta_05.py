"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        values = {}
        for row in csv.reader(file, delimiter="\t"):
            num = int(row[1])
            if row[0] not in values:
                values[row[0]] = [num, num]
            else:
                values[row[0]][0] = max(values[row[0]][0], num)
                values[row[0]][1] = min(values[row[0]][1], num)

        return sorted([(key, val[0], val[1]) for key, val in values.items()])

