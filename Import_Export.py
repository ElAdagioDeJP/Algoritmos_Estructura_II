import json, os
import ejemplo as ej


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