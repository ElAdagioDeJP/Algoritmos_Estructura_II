import Main as main
main = main.modificar()


class Menu:
    def __init__(self):
        self.opciones = []
        self.titulo = ""
        self.menu = ""
        self.opcion = 0
        self.salir = False
        self.opcion = 0

    def Mostrar_Menu(self):
        while True:
            print("********************************************************************")
            print("     ------------Bienvenido al sistema administrativo-----------    ")
            print("********************************************************************")
            print("")
            print("¿Qué desea hacer?")
            print("1. Crear Proyecto")
            print("2. Modificar Proyecto")
            print("3. Consultar Proyecto")
            print("4. Eliminar Proyecto")
            print("5. Listar Proyectos")
            print("6. Agregar Tarea")
            print("7. Tareas")
            print("8. Reporte")
            print("9. Salir")
            print("")
            print("-----------------------------------------------")
            print("")
            opcion = int(input("Ingrese la opción deseada (1-9): "))
            def Comprobacion(self, opcion):
                while True:
                    try:
                        if 1 <= opcion <= 9:
                            return opcion
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-9): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-9): "))
                
            if self.opcion == 1: #Crear Proyecto
                print("")
                print("Crear Proyecto")
                
            elif self.opcion == 2: #Modificar Proyecto
                print("")
                print("Modificar Proyecto")
                
            elif self.opcion == 3: #Consultar Proyecto
                print("")
                print("Consultar Proyecto")
                
            elif self.opcion == 4: #Eliminar Proyecto
                print("")
                print("Eliminar Proyecto")
                
            elif self.opcion == 5: #Listar Proyectos
                print("")
                print("Listar Proyectos")
                
            elif self.opcion == 6: #Agregar Tarea
                print("")
                print("¿En que proyecto de desea agregar las tareas?\n")
                print("Nombre de los proyectos: \n")
                cont = main.Imprimir_Proyectos()
                print("")
                opcion = Comprobacion(opcion)
                
                #f opcion = :
                    
            elif self.opcion == 7:
                print("")
                print("Tareas")
                main.ordenar_tareas_colas()
                
                
            elif self.opcion == 8:
                print("")
                print("Reporte")
                
            elif self.opcion == 9:
                print("")
                print("Desea guardar los cambios realizados?")
                print("1. Si")
                print("2. No")
                guardar = input("Ingrese la opción deseada (1-2): ")
                if guardar == "1":
                    print("Guardando cambios...")
                    break
                elif guardar == "2":
                    print("Saliendo sin guardar cambios...")
                    break
                
        
        
menu = Menu()
menu.Mostrar_Menu()