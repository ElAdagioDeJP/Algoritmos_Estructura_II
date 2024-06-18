class Menu:
    def __init__(self):
        self.opciones = []
        self.titulo = ""
        self.menu = ""
        self.opcion = 0
        self.salir = False
    def Mostrar_Menu(self):
        while True:
            print("********************************************************************")
            print("-----------Bienvenido al sistema de manejo administrativo-----------")
            print("********************************************************************")
            print("")
            print("¿Qué desea hacer?")
            print("1. Crear Proyecto")
            print("2. Modificar Proyecto")
            print("4. Consultar Proyecto")
            print("5. Eliminar Proyecto")
            print("6. Listar Proyectos")
            print("7. Tareas")
            
        
        
meniu = Menu()
meniu.Mostrar_Menu()