class Proyectos:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_fin, estado, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.listilla = []
    def __str__(self):
        return f'{self.id} {self.nombre} {self.descripcion} {self.fecha_inicio} {self.fecha_fin} {self.estado} {self.empresa} {self.gerente} {self.equipo}'
    def listaentre(self):
        self.listilla.append(self.id)
        self.listilla.append(self.nombre)
        self.listilla.append(self.descripcion)
        self.listilla.append(self.fecha_inicio)
        self.listilla.append(self.fecha_fin)
        self.listilla.append(self.estado)
        self.listilla.append(self.empresa)
        self.listilla.append(self.gerente)
        self.listilla.append(self.equipo)
        return self.listilla
    def getlistilla(self):
        return 
class listagrande:
    def __init__(self):
        
        self.lista = []
    def agregar(self):
       
       while True:

            respuesta = input("desea agregar un proyecto? (s/n): ")
            if respuesta.lower() == 's':
                id = input(str("ingrese el id del proyecto: "))
                nombre = input(str("ingrese el nombre del proyecto: "))
                descripcion = input(str("ingrese la descripcion del proyecto: "))
                fecha_inicio = input(str("ingrese la fecha de inicio del proyecto: "))
                fecha_fin = input(str("ingrese la fecha de fin del proyecto: "))
                estado = input(str("ingrese el estado del proyecto: "))
                empresa = input(str("ingrese la empresa del proyecto: "))
                gerente = input(str("ingrese el gerente del proyecto: "))
                equipo = []
                while True:
                    equipo.append(input(str("ingrese el equipo del proyecto: ")))
                    ag = input("desea agregar mas personas? (s/n): ")
                    if ag.lower() == 'n':
                        break
                    elif ag.lower() != 's':
                        print("Porfavor elegir una opcion valida")
                        ag = input("desea agregar mas personas? (s/n): ")
                proyecto = Proyectos(id, nombre, descripcion, fecha_inicio, fecha_fin, estado, empresa, gerente, equipo)
                self.lista.append(proyecto.listaentre())
                    
            elif respuesta.lower() == 'n':
                print("Gracias por usar el programa")
                self.mostrar()
                break
                
                
            else:
                print("Por favor, ingrese 's' para agregar un nuevo proyecto o 'n' para terminar.") 

    def mostrar(self):
        for proyecto in self.lista:
            print("1. " + proyecto)
    def borrar(self):
        eliminar = input(int("ingrese la posicion del proyecto que desea eliminar: "))
        self.lista.pop(eliminar -1)
        
class Principal:
    def eleccion(self):
        while True:
            self.eleccion = input("desea agregar un proyecto, ver la lista de proyectos, modificar un proyecto, eliminar un proyecto o salir? (agregar/ver/modificar/eliminar/salir): ")
            if self.eleccion.lower() == 'agregar':
                lista = listagrande()
                lista.agregar()
            elif self.eleccion.lower() == 'ver':
                print(lista.mostrar())
            elif self.eleccion.lower() == 'modificar':
                print("En construccion")
            elif self.eleccion.lower() == 'eliminar':
                print("En construccion")
            elif self.eleccion.lower() == 'salir':
                print("Gracias por usar el programa")
                break
            else:
                print("Por favor, ingrese 'agregar', 'ver', 'modificar' o 'eliminar'.")
lista = listagrande()
lista.agregar()

