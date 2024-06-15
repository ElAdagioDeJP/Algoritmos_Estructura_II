class Proyectos:
    def __init__(self):
        self.id = input(str("ingrese el id del proyecto: "))
        self.nombre = input(str("ingrese el nombre del proyecto: "))
        self.descripcion = input(str("ingrese la descripcion del proyecto: "))
        self.fecha_inicio = input(str("ingrese la fecha de inicio del proyecto: "))
        self.fecha_fin = input(str("ingrese la fecha de fin del proyecto: "))
        self.estado = input(str("ingrese el estado del proyecto: "))
        self.empresa = input(str("ingrese la empresa del proyecto: "))
        self.gerente = input(str("ingrese el gerente del proyecto: "))
        self.equipo = input(str("ingrese el equipo del proyecto: "))
        listilla = []
    def __str__(self):
        return f'{self.id} {self.nombre} {self.descripcion} {self.fecha_inicio} {self.fecha_fin} {self.estado} {self.empresa} {self.gerente} {self.equipo}'
    def listaentre(self):
        listilla = []
        listilla.append(self.id)
        listilla.append(self.nombre)
        listilla.append(self.descripcion)
        listilla.append(self.fecha_inicio)
        listilla.append(self.fecha_fin)
        listilla.append(self.estado)
        listilla.append(self.empresa)
        listilla.append(self.gerente)
        listilla.append(self.equipo)
        return listilla
class listagrande:
    def __ini__(self):
        
        self.lista = []
    def agregar(self):
       while True:

            respuesta = input("desea agregar un proyecto? (s/n): ")
            if respuesta.lower() == 's':
                proyecto = Proyectos()
                self.lista.append(proyecto.listaentre())

            elif respuesta.lower() == 'n':
                print("Gracias por usar el programa")
                break
                
            else:
                print("Por favor, ingrese 's' para agregar un nuevo proyecto o 'n' para terminar.") 

    def mostrar(self):
        for proyecto in self.lista:
            print(proyecto)

lista = listagrande()
lista.agregar()
lista.mostrar()

