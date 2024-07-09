import EmpresaProyectos
import datetime
import json
Empresas_Proyectos = EmpresaProyectos.AVLTree()
Proyectos_Tareas = EmpresaProyectos.AVLTree()

class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = EmpresaProyectos.ListaEnlazada()
        
    def agregar_proyecto(self, proyecto):
        self.proyectos.agregar(proyecto)
        
class Proyectos:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.tareas = EmpresaProyectos.ListaEnlazada()
    
    def agregar_tarea(self, tarea):
        self.tareas.agregar(tarea)
        
    def calcular_p(self):
        if len(self.tareas) > 0:
            self.p = self.porcenta / len(self.tareas)
        else:
            self.p = 0
        
class Tareas:
    def __init__(self, id, nombre,  cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual):
        self.id = id
        self.nombre = nombre
        self.cliente = cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.subtareas = EmpresaProyectos.ListaEnlazada()
    def agregar_subtareas(self, subtarea):
        
        self.subtareas.agregar(subtarea)

class subTareas:
    def __init__(self, id, nombre, empresa,  cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.sub_subtareas= EmpresaProyectos.ListaEnlazada()

    



def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyectos(
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
                tarea = Tareas(
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
                    subtarea = subTareas(
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                        subtarea_data["descripcion"],
                        subtarea_data["estado"]
                    )
                    tarea.agregar_subtareas(subtarea)
                proyecto.agregar_tarea(tarea)
            proyecto.calcular_p()
            proyectos.append(proyecto)
    return proyectos

class iniciar():
    def __init__(self):   #Para que funcione necesita la direccion directa del archivo json
        ruta_archivo = "C:/Users/ElAdagioDeJP/Documents/GitHub/Algoritmos_Estructura_II/Sistema Gestion Arboles Binarios/datos.json"
        #ruta_archivo_subtarea = os.path.join(os.getcwd(), "Proyectos_Algoritmos_2/datos_subtareas.json")
        self.proyectox = cargar_datos_desde_json(ruta_archivo)
        #self.proyectox_subtarea = cargar_datos_desde_json(ruta_archivo_subtarea)
    #def ver():
    def agregarAEmpresa(self):
        self.empresax = Empresa()
        for i in self.proyectox:
            if i.id == "1":
                self.empresax.agregar_proyecto(i)


iniciar = iniciar()
                
iniciar.agregarAEmpresa()
    