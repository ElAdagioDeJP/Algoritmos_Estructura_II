

class Menu:
    def __init__(self):
        self.arbol = None
        
    def Validar(self):
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                print("")
                break
            except ValueError:
                print("Error: Ingrese numeros.")
        return opcion
    def ConsultarPor(self):
        print("")
        print("1. ID")
        print("2. Nombre")
        print("3. Gerente")
        print("4. Fecha de Inicio")
        print("5. Fecha de Vencimiento")
        print("6. Estado Actual")
        print("7. Regresar al Menu 'Inicial'")
        print("")
                     
    def verMenu(self): #Menu principal del proyecto
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||||||||||Bienvenido al Gestor||||||||||||||||")
        print("||||||||||||||Administrativo 777|||||||||||||||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        print("¿Que desea gestionar?\n")
        print("1. Empresas")
        print("2. Proyectos")
        print("3. Tareas")
        print("4. SubTareas")
        print("5. Reportes")
        print("6. Salir")
        opcion = self.Validar()
        print("")
        
        if opcion == 1: #Menu para las Empresas
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            print("|||||||||||||||Gestor de Empresas||||||||||||||||")
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            print("1. Crear Empresa")
            print("2. Listar Empresas")
            print("3. Modificar Empresa")
            print("4. Consultar Empresa")
            print("5. Eliminar Empresa")
            print("6. Regresar al menu 'x nro'")
            opcion = self.Validar()
            print("")
            if opcion == 1: # Las diferentes opciones para realizar en las Empresas
                print("...Desea Crear una Empresa \n")
                
            elif opcion == 2:
                print("...Desea enlistar todas las Empresas \n")
                
            elif opcion == 3:
                print("...Desea Modificar una Empresa \n")
                
            elif opcion == 4:
                print("...Desea Consultar alguna Empresa \n")
            
            elif opcion == 5:
                print("...Desea Eliminar una Empresa \n")
                
            else:
                print("")
                print("Regresando al menu principal\n")
                
        elif opcion == 2: #Menu Para los proyectos
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            print("|||||||||||||||Gestor de Proyectos|||||||||||||||")
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            print("1. Crear Proyecto")
            print("2. Listar Proyecto")
            print("3. Modificar Proyecto")
            print("4. Consultar Proyecto")
            print("5. Eliminar Proyecto")
            print("Regresar al Menu 'x nro'")
            opcion = self.Validar()
            print("")
            
            if opcion == 1: # Las diferentes opciones para realizar en los Proyectos
                print("...Desea Crear un Proyecto \n")
                
            elif opcion == 2:
                print("...Desea enlistar todos los proyectos \n")
                print("Por: \n")
                self.ConsultarPor()
                opcion2 = self.Validar()
                
                
            elif opcion == 3:
                print("...Desea Modificar un Proyecto \n")
                print("Por: \n")
                self.ConsultarPor()
                opcion2 = self.Validar()
                
                if opcion2 == 1:
                    print("Modificando por ID")
                elif opcion2 == 2:
                    print("Modificando por Nombre")
                elif opcion2 == 3:
                    print("Modificando por Gerente")
                elif opcion2 == 4:
                    print("Modificando por Fecha de Inicio")
                elif opcion2 == 5:
                    print("Modificando por Fecha de Vencimiento")
                elif opcion2 == 6:
                    print("Modificando por el Estado Actual")
                else:
                    print("Regresando al menu\n")
                    self.verMenu()

            elif opcion == 4:
                print("...Desea Consultar algun Proyecto")
                print("Consulte por: \n")
                self.ConsultarPor()
                opcion2 = self.Validar()
                print("")
                
                if opcion2 == 1:
                    print("Consultando por ID")
                elif opcion2 == 2:
                    print("Consultando por Nombre")
                elif opcion2 == 3:
                    print("Consultando por Gerente")
                elif opcion2 == 4:
                    print("Consultando por Fecha de Inicio")
                elif opcion2 == 5:
                    print("Consultando por Fecha de Vencimiento")
                elif opcion2 == 6:
                    print("Consultando por el Estado Actual")
                else:
                    print("Regresando al menu\n")
                    self.verMenu()
            
            elif opcion == 5:
                print("...Desea Eliminar una Empresa \n")
                print("Por: \n")
                self.ConsultarPor()
                opcion2 = self.Validar()
                
                if opcion2 == 1:
                    print("Eliminando por ID")
                elif opcion2 == 2:
                    print("Eliminando por Nombre")
                elif opcion2 == 3:
                    print("Eliminando por Gerente")
                elif opcion2 == 4:
                    print("Eliminando por Fecha de Inicio")
                elif opcion2 == 5:
                    print("Eliminando por Fecha de Vencimiento")
                elif opcion2 == 6:
                    print("Eliminando por el Estado Actual")
                else:
                    print("Regresando al menu\n")
                    self.verMenu()
                
            else:
                print("")
                print("Regresando al menu principal\n")

        elif opcion == 3:
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||||||||||||||Gestor de Tareas|||||||||||||||||")
            print("|||||||||||||||||||||||||||||||||||||||||||||||||")
            

        elif opcion == 4:
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||||||||||||||Gestor de subTareas|||||||||||||||||")
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||")

        elif opcion == 5:
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||||||||||||||||| Reportes |||||||||||||||||||||||")
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
        elif opcion == 6:
            return
        else:
            print('Seleccione alguna opcion') 
            self.verMenu()
            
menu = Menu()
menu.verMenu()