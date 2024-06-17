from datetime import datetime
import json

class Proyecto:    
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []
        self.porcenta = 0
        self.p = 0

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        self.porcenta += tarea.porcentaje
        
    def calcular_p(self):
        if len(self.tareas) > 0:
            self.p = self.porcenta / len(self.tareas)
        else:
            self.p = 0
    
        

class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.porcentaje = porcentaje
        self.subtareas = []

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        
def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyecto(
                proyecto_data["id"],
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                datetime.strptime(proyecto_data["fecha_inicio"], "%Y-%m-%d"),
                datetime.strptime(proyecto_data["fecha_vencimiento"], "%Y-%m-%d"),
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            for tarea_data in proyecto_data["tareas"]:
                tarea = Tarea(
                    tarea_data["id"],
                    tarea_data["nombre"],
                    tarea_data["empresa_cliente"],
                    tarea_data["descripcion"],
                    datetime.strptime(tarea_data["fecha_inicio"], "%Y-%m-%d"),
                    datetime.strptime(tarea_data["fecha_vencimiento"], "%Y-%m-%d"),
                    tarea_data["estado"],
                    tarea_data["porcentaje"]
                )
                for subtarea_data in tarea_data.get("subtareas", []):
                    subtarea = Subtarea(
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                        subtarea_data["descripcion"],
                        subtarea_data["estado"]
                    )
                    tarea.agregar_subtarea(subtarea)
                proyecto.agregar_tarea(tarea)
            proyecto.calcular_p()
            proyectos.append(proyecto)
    return proyectos



class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0
    def __len__(self):
        return self.longitud
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente
            
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
        
    def eliminar(self, valor):
        if self.cabeza is None:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False
    
    def insertar(self, indice, valor):
        if indice < 0 or indice > self.longitud:
            raise IndexError("Índice fuera de rango")
        nuevo_nodo = Nodo(valor)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
        
    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def index(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError("{} no está en la lista".format(valor))
    
    def pop(self, indice=None):
        if indice is None:
            indice = self.longitud - 1
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            varsalor = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return valor
        actual = self.cabeza
        for i in range(indice - 1):
            actual = actual.siguiente
        valor = actual.siguiente.valor
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1
        return valor
    


class modificar:
    def __init__(self):    
        ruta_archivo = "./datos_prueba.json"
        self.proyectox = cargar_datos_desde_json(ruta_archivo)
        
                
    def filtrar_tareas_por_rango(self, fecha_inicio, fecha_fin):
        tareas_filtradas = []
        for proyecto in self.proyectox:
            for tarea in proyecto.tareas:
                if fecha_inicio <= tarea.fecha_inicio <= fecha_fin:
                    tareas_filtradas.append(tarea)
        return tareas_filtradas
        
    def filtrar_proyectos_por_rango(self, proyectos, fecha_inicio, fecha_fin):
        proyectos_f = []
        for proyecto in self.proyectox:
            if fecha_inicio <= proyecto.fecha_inicio <= fecha_fin:
                proyectos_f.append(proyecto)
        return proyectos_f  

    def filtrar_por_id(self):
        id_proyecto = int(input("Ingrese el id del proyecto: "))
        for proyecto in self.proyectox:
            if proyecto.id == id_proyecto:
                return proyecto
            
    def agregar_huevonadas(self):
        id = int(input("Ingrese el id del proyecto: "))
        nombre = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripcion del proyecto: ")
        fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto: "), "%Y-%m-%d")
        fecha_vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto: "), "%Y-%m-%d")
        estado = input("Ingrese el estado del proyecto: ")
        empresa = input("Ingrese la empresa del proyecto: ")
        gerente = input("Ingrese el gerente del proyecto: ")
        equipo = input("Ingrese el equipo del proyecto: ")
        proyecto = Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
        
        tareita= self.agregar_tareasx(proyecto)
        
        proyecto.agregar_tarea(tareita)    
        self.proyectox.append(proyecto)
        
    
    def eliminando_huevonadas(self):
        print("Proyectos: ")
        for proyectos in self.proyectox:
            print(proyectos.nombre)
        eli = int(input("Cual Proyecto desea eliminar: "))
        eli -= 1
        self.proyectox.pop(eli)
    
    def mostrar_huevonadas(self):
         for proyectos in self.proyectox:
            print(proyectos.nombre)
            for tarea in proyectos.tareas:
                print(tarea.nombre)
                for subtarea in tarea.subtareas:
                    print(subtarea.nombre)

    def agregar_tareasx(self, proyectoy):
        listoca = ListaEnlazada()
        for tarea in proyectoy.tareas:
            listoca.agregar(tarea)
        i = int(input("Cuantas tareas desea agregar: "))
        a = input("Desea agregar las tareas en una posicion especifica? s/n: ")
        if a =="n":
            while i !=0:
                idt = input("Ingrese el id de la tarea: ")
                nombret = input("Ingrese el nombre de la tarea: ")
                empresa_clientet = input("Ingrese la empresa del cliente: ")
                descripciont = input("Ingrese la descripcion de la tarea: ")
                fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio de la tarea: "), "%Y-%m-%d")
                fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento de la tarea: "), "%Y-%m-%d")
                estadot = input("Ingrese el estado de la tarea: ")
                porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
                tareita = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
                j = int(input("Cuantas subtareas desea agregar: "))
                
                while j !=0:
                    
                    ids = input("Ingrese el id de la subtarea: ")
                    nombres = input("Ingrese el nombre de la subtarea: ")
                    descripcions = input("Ingrese la descripcion de la subtarea: ")
                    estados = input("Ingrese el estado de la subtarea: ")
                    subtareita = Subtarea(ids, nombres, descripcions, estados)
                    tareita.agregar_subtarea(subtareita)
                    j -= 1
                    
                listoca.agregar(tareita)
                i -= 1
                for ele in listoca:
                    print(ele , end = "")
            return listoca
        elif a == "s":
            for ele in listoca:
                print(ele , end = "")
            posi = int(input("En que posición desea insertar la tarea? "))
            posi -= 1
            while i !=0:
                idt = input("Ingrese el id de la tarea: ")
                nombret = input("Ingrese el nombre de la tarea: ")
                empresa_clientet = input("Ingrese la empresa del cliente: ")
                descripciont = input("Ingrese la descripcion de la tarea: ")
                fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio de la tarea: "), "%Y-%m-%d")
                fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento de la tarea: "), "%Y-%m-%d")
                estadot = input("Ingrese el estado de la tarea: ")
                porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
                tareita = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
                j = int(input("Cuantas subtareas desea agregar: "))
                
                while j !=0:
                    
                    ids = input("Ingrese el id de la subtarea: ")
                    nombres = input("Ingrese el nombre de la subtarea: ")
                    descripcions = input("Ingrese la descripcion de la subtarea: ")
                    estados = input("Ingrese el estado de la subtarea: ")
                    subtareita = Subtarea(ids, nombres, descripcions, estados)
                    tareita.agregar_subtarea(subtareita)
                    j -= 1
                    
                listoca.insertar(posi,tareita)
                i -= 1
                for ele in listoca:
                    print(ele , end = "")
            return listoca

        
print("Me comí una salchipapa, Ay que cosa tan sabrosa, y se me quedó en la garganta porque no me quedó para la gaseosa \n"
      +"Me comí una salchipapa, Ay que cosa tan sabrosa, y se me quedó en la garganta porque no me quedó para la gaseosa\n"+
        "Me comí una salchipapa, Ay que cosa tan sabrosa, y se me quedó en la garganta porque no me quedó para la gaseosa\n"+
        "Me comí una salchipapa, Ay que cosa tan sabrosa, y se me quedó en la garganta porque no me quedó para la gaseosa")


proyecto = modificar()
proyecto.agregar_huevonadas()
proyecto.mostrar_huevonadas()
"""
# Ejemplo de uso:

# Creamos algunos objetos de la clase Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Accord")
carro3 = Carro("Ford", "Mustang")
carro4 = Carro("Chevrolet", "Camaro")

# Creamos la lista enlazada y agregamos algunos carros
autos = ListaEnlazada()
autos.agregar(carro1)
autos.agregar(carro2)
autos.agregar(carro3)

lista = list(autos)
"""
