import json, os
import ejemplo as ej

ej.crear_proyecto('Proyecto 1', '2021-10-10', '2021-10-20', 'Proyecto de prueba', 'Proyecto 1')

def cargar_configuracion(config_path='config.txt'):
    configuracion = {}
    with open(config_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            configuracion[key] = value
    return configuracion

def cargar_datos(datos_path):
    with open(datos_path, 'r') as file:
        return json.load(file)

def guardar_datos(datos, datos_path):
    with open(datos_path, 'w') as file:
        json.dump(datos, file, indent=4)

def cargar_subtareas(subtareas_path):
    with open(subtareas_path, 'r') as file:
        return json.load(file)