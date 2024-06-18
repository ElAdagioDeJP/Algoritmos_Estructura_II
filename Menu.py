

class Menu:
    def __init__(self):
        self.opciones = []
    def Mostrar_menu(self):
        for opcion in self.opciones:
            print(opcion)