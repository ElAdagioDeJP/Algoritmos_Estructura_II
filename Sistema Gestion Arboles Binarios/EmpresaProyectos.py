import csv
import os
from datetime import datetime
import json, os
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
    

        
    
class AVLNode:
    def __init__(self, key, project):
        self.key = key
        self.project = project
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key, project):
        if not root:
            return AVLNode(key, project)
        elif key < root.key:
            root.left = self.insert(root.left, key, project)
        else:
            root.right = self.insert(root.right, key, project)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


lista_enla = ListaEnlazada()    
Archivo = UtilizarArchivo()
Archivo.ExportarArchivo(lista_enla)


def ModificarCsv():
    with open('Data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in lista_enla:
            writer.writerow(i)
                                                
ModificarCsv()
