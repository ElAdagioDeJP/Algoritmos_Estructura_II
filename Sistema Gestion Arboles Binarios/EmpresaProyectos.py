import csv
import os

# Verificar el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())

# Cambiar el directorio de trabajo si es necesario
os.chdir('C:/Users/ElAdagioDeJP/Documents/GitHub/Algoritmos_Estructura_II/Sistema Gestion Arboles Binarios')
print("Directorio de trabajo después de cambiar:", os.getcwd())

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
    
    def modificardato(self, indice_buscar, new_valor, indice):
        self.valor_lista = self.obtener(indice_buscar)
        self.valor_lista[indice] = new_valor
        self.pop(indice_buscar)
        self.insertar(indice_buscar, self.valor_lista)
        
    def modificartodo(self, indice, valor_lista):
        self.valor_lista = valor_lista
        self.pop(indice)
        self.insertar(indice, self.valor_lista)
        
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

class UtilizarArchivo: 
    def __init__(self):
        pass
    def ExportarArchivo(self, valor):
        self.valor = valor
        with open('Data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.valor.agregar(row)

    def Imprimir(self):
        for i in self.valor:
            print(i)
            
    def Lencsv(self):
        cont = 0
        with open('Data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                cont += 1
        return cont + 1

class NodoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre
        
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAvl:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def insertar(self, nodo, nombre):
        if not nodo:
            return NodoArchivo(nombre)

        if nombre < nodo.nombre:
            nodo.izquierda = self.insertar(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self.insertar(nodo.derecha, nombre)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_balance(nodo)

        if balance > 1 and nombre < nodo.izquierda.nombre:
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre > nodo.derecha.nombre:
            return self.rotar_izquierda(nodo)

        if balance > 1 and nombre > nodo.izquierda.nombre:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre < nodo.derecha.nombre:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def insertar_archivo(self, nombre):
        self.raiz = self.insertar(self.raiz, nombre)

    def inorder(self, nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.nombre)
            self.in_order(nodo.derecha)

lista_enla = ListaEnlazada()    
Archivo = UtilizarArchivo()
Archivo.ExportarArchivo(lista_enla)
lista_prueba = ([1, 'Juan', 'Perez', 'Ingeniero', 'Desarrollador', 'Proyecto 1', 'Proyecto 2', 'Proyecto 3', 'Proyecto 4', 'Proyecto 5'],)
arbolavl = ArbolAvl()

arbolavl.insertar_archivo(10)
arbolavl.insertar_archivo(20)
arbolavl.insertar_archivo(30)
arbolavl.insertar_archivo(40)
arbolavl.insertar_archivo(50)
arbolavl.insertar_archivo(25)

arbolavl.inorder()

def ModificarCsv():
    with open('Data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in lista_enla:
            writer.writerow(i)
            
ModificarCsv()
