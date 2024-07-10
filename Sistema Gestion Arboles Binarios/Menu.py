import EmpresaProyectos

datos = EmpresaProyectos
lista_enla = datos.ListaEnlazada()

archivo = datos.UtilizarArchivo()
modificar = datos.ModificarCsv()
archivo.ExportarArchivo(lista_enla)

class Menu:
    def __init__(self):
        self.arbol = None
        
    def Validar(self):
        while True:
            try:
                print("")
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
                print("...Desea Crear una Empresa")
                print("Ingrese los datos de la nueva Empresa: \n")
                Id = archivo.Lencsv()
                nombre = input("Nombre de la Empresa: ")
                descripcion = input("Descripcion de la Empresa: ")
                fecha_creacion = input("Fecha de Creacion de la Empresa: ")
                direccion = input("Direccion de la Empresa: ")
                telefono = input("Telefono de la Empresa: ")
                correo = input("Correo de la Empresa: ")
                gerente = input("Nombre del Gerente de la Empresa: ")           
                equipo_contacto = input("Equipo de Contacto de la Empresa: ")
                lista_enla.agregar([Id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto])
                datos.ModificarCsv()
            elif opcion == 2:
                
                archivo.Imprimir()
                
                
            elif opcion == 3:
                print("...Desea Modificar una Empresa \n")
                print("Por: \n")
                print("1. Modificar un Dato de la Empresa")
                print("2. Modificar Toda la Empresa")
                print("3. Regresar al Menu 'Inicial'")
                opcion2 = self.Validar()
                
                
                if opcion2 == 1:
                    
                    print("¿Que dato desea modificar?")
                    print("1. ID")
                    print("2. Nombre")
                    print("3. Descripcion")
                    print("4. Fecha de Creacion")
                    print("5. Direccion")
                    print("6. Telefono")
                    print("7. Correo")
                    print("8. Gerente")
                    print("9. Equipo de Contacto")
                    print("10. Regresar al Menu 'Inicial'")
                    opcion3 = self.Validar()
                    indice = int(input("Que lista quieres modificar: "))
                    indice -= 1
                    if opcion3 == 1:
                        opcion3 -=1
                        print("Modificando el ID")
                        datinho = int(input("Ingrese el nuevo ID: "))
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 2:
                        print("Modificando el Nombre")
                        opcion3 -= 1
                        datinho = input("Ingrese el nuevo Nombre: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 3:
                        print("Modificando la Descripcion")
                        
                        opcion3 -=1
                        datinho = input("Ingrese el nuevo Descripcion: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 4:
                        opcion -=1
                        datinho = input("Ingrese el nuevo Fecha de  Creacion: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 5:
                        opcion -=1
                        datinho = input("Ingrese la nueva direccion: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 6:
                        opcion -=1
                        datinho = input("Ingrese el nuevo telefono: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 7:   
                        
                        opcion -=1
                        datinho = input("Ingrese el nuevo correo: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 8:   
                        
                        opcion -=1
                        datinho = input("Ingrese el nuevo gerente: ")
                        lista_enla.modificardato(indice,datinho,opcion3)
                    elif opcion3 == 9:   
                        
                        opcion -=1
                        datinho = input("Ingrese el nuevo equipo de contacto: ")
                        
                        lista_enla.modificardato(indice,datinho,opcion3)
                    
                elif opcion2 == 2:
                    indice = int(input("Que lista quieres modificar: "))
                    indice -= 1
                    print("Ingrese los datos de la nueva Empresa: \n")
                    Id = archivo.Lencsv()
                    nombre = input("Nombre de la Empresa: ")
                    descripcion = input("Descripcion de la Empresa: ")
                    fecha_creacion = input("Fecha de Creacion de la Empresa: ")
                    direccion = input("Direccion de la Empresa: ")
                    telefono = input("Telefono de la Empresa: ")
                    correo = input("Correo de la Empresa: ")
                    gerente = input("Nombre del Gerente de la Empresa: ")           
                    equipo_contacto = input("Equipo de Contacto de la Empresa: ")
                    lista_enla.modificartodo(indice,[Id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto])
                    datos.ModificarCsv()
                               
                                    
            elif opcion == 4:
                print("...Desea Consultar alguna Empresa \n")
                
            elif opcion == 5:
                print("...Desea Eliminar una Empresa \n")
                indice = int(input("Colocar indice: "))
                
                lista_enla.pop(indice)
                
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
                    ide = int(input("Ingrese un id: "))
                    lista_enla.obtener(ide)
                    archivo.Imprimir()
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
            
        
        if opcion == 6:
            return
        
        self.verMenu()
            
menu = Menu()
menu.verMenu()
