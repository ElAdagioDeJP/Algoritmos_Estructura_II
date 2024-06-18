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
            self.opcion = Comprobacion(self, opcion)
                
            if self.opcion == 1: #Crear Proyecto
                print("")
                print("Creacion de Proyecto \n")
                print("")                
                main.Agregar_Proyectos()
                
            elif self.opcion == 2: #Modificar Proyecto
                print("")
                print("Modificar Proyecto")
                
            elif self.opcion == 3: #Consultar Proyecto
                print("")
                print("Consultar Proyecto")
                
            elif self.opcion == 4: #Eliminar Proyecto
                print("")
                print("Eliminar Proyectos")
                print("")
                print("¿Qué proyecto desea eliminar?\n")
                main.Imprimir_Proyectos()
                print("")
                opcion = int(input("Ingrese la opción deseada (1-9): "))
                while True:
                    try:
                        if 1 <= opcion <= 9:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-9): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-9): "))
                main.Eliminar_Proyectos(opcion)
                print("Proyecto eliminado con éxito")
                print("")
                main.Imprimir_Proyectos()
                
                
                
            elif self.opcion == 5: #Listar Proyectos
                print("")
                print("Listar Proyectos")
                print("")
                main.Imprimir_Proyectos()
                print("")
                
            elif self.opcion == 6: #Agregar Tarea
                print("")
                print("¿En que proyecto de desea agregar las tareas?\n")
                print("Nombre de los proyectos: \n")
                cont = main.Imprimir_Proyectos()
                print("")
                opcion = int(input("Ingrese la opción deseada (1-9): "))
                while True:
                    try:
                        if 1 <= opcion <= 9:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-9): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-9): "))
                
                #f opcion = :
                    
            elif self.opcion == 7:
                print("")
                print("Estas en el menu de Tareas\n")
                print("¿Qué desea hacer?\n")
                print("1. Agregar Tareas al final")
                print("2. Agregar Tareas en una posición específica")
                print("3. Modificar Tarea")
                print("4. Eliminar Tarea")
                print("5. Listar Tareas")
                
                opcion = int(input("Ingrese la opción deseada (1-5): "))
                while True:
                    try:
                        if 1 <= opcion <= 5:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-5): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-5): "))
                        
                
                
                
                
                
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