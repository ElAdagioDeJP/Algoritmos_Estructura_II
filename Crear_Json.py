import json

def Guardar_json(proyecto):
    try:
        with open('data.json', 'w') as archivo:
            json.dump(proyecto, archivo, indent=4)
    except FileNotFoundError:
        print("No se encontro el archivo deah 😈")
        
"""
data = {}
data['Empresa'] = []
data['Empresa'].append({
    "Proyecto": [],
    
    
})"""