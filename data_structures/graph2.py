#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
"""
Module description goes here

"""

from .Cola  import *
import math
from heapq import heappush, heappop

# Se inicializa una lista vacía como cola de prioridad (priority queue) para usarse en
# el algoritmo de Dijkstra, para esto se importa la librería heapq con los métodos heap
# push y heap pop
cola_prioridad = []
# Diccionario que guardan el nodo padre de cada nodo al usar el método Kruskal
parent = dict()
# Diccionario que guardan el rank de cada nodo al usar el método Kruskal
rank = dict()

class Vertice(object):
    """ Esta es una clase vértice que representa un nodo en un grafo.

    """

    def __init__(self, label=None):
        # Etiqueta del vértice
        self.label = label
        # Lista de adyacencia del vértice
        self.lista_vecinos = []

        # Distancias hacia los vecinos
        self.lista_pesos = []
        # Grado del vértice
        self.grado = 0
        # Atributos para los métodos BFS, DFS y Dijkstra
        self.estado = "NO VISITADO"
        # Esta distancia hace referencia a los niveles de diferencia entre el nodo
        # y la raíz en BFS
        self.distancia = None
        self.padre = None
        self.totalDistance = float('Inf')


    def añadir_adyacentes(self, vecino, peso):
        """ Añade vecinos al vértice

        """

        if vecino not in self.lista_vecinos:
            self.lista_vecinos.append(vecino)
            self.lista_pesos.append(peso)
            self.grado += 1

    def __lt__(self, other):
        """ Evita que se presenten errores al comparar vértices con misma
           prioridad en la instrucción que usa heappush en dijkstra

        """
        return int(self.label) < int(other.label)

class Graph2(object):
    """ Esta es una clase Grafo que representa un grafo.

    """

    def __init__(self, label):
        # Etiqueta del grafo
        self.label = label
        self.lista_vertices = []
        # Grado del grafo
        self.grado = 0
        self.numero_aristas = 0
        self.numero_vertices = 0
        self.edges = []

    def añadir_aristas(self, vertice1, vertice2, peso=1):
        """ Añade aristas al grafo

        """

        vertices = [item.label for item in self.lista_vertices]
        if vertice1 not in vertices:
            self.añadir_vertice(vertice1)
        if vertice2 not in vertices:
            self.añadir_vertice(vertice2)
        vertice1_existente = self.get_vertice(vertice1)
        vertice1_existente.añadir_adyacentes(vertice2, peso)
        vertice2_existente = self.get_vertice(vertice2)
        vertice2_existente.añadir_adyacentes(vertice1, peso)
        self.numero_aristas += 1
        tupla = (peso, vertice1, vertice2)
        self.edges.append(tupla)

    def add_vertex_dir(self, vertice1, vertice2, peso=1):
        """ Añade aristas dirigidas al grafo

        """

        vertices = [item.label for item in self.lista_vertices]
        if vertice1 not in vertices:
            self.añadir_vertice(vertice1)
        if vertice2 not in vertices:
            self.añadir_vertice(vertice2)
        vertice1_existente = self.get_vertice(vertice1)
        vertice1_existente.añadir_adyacentes(vertice2, peso)
        self.numero_aristas += 1
        # El cero como último parametro representa el flujo inicial en Ford-Fulkerson
        lista = [peso, vertice1, vertice2, 0]
        self.edges.append(lista)

    def get_vertice(self, label):
        """ Regresa el objeto tipo Vértice dada su etiqueta

        """

        find = False
        for item in self.lista_vertices:
            if item.label == label:
                find = True
                return item
        if not find:
            return False

    def add_vertex(self, label):
        """ Añade vértices al grafo

        """

        vertices = [item.label for item in self.lista_vertices]
        if label not in vertices:
            nuevo_vertice = Vertice(label)
            self.lista_vertices.append(nuevo_vertice)
            self.numero_vertices += 1

    def BFS(self, root):
        """ Realiza una busqueda en anchura dado un nodo raíz

        """
        self.ResetEstados()
        print("")
        print("Busqueda en anchura con vertice raiz = " + root)
        nodo = self.get_vertice(root)
        # Atributos de inicio para nodo raíz
        nodo.estado = "VISITADO"
        nodo.distancia = 0
        nodo.padre = None

        # Se encola el nodo raíz
        ColaQ = Cola()
        if ColaQ.es_vacia():
            ColaQ.encolar(nodo)

        while not ColaQ.es_vacia():
            nodoU = ColaQ.desencolar()
            # Para cada nodo que se extrae de la cola, se obtiene su lista de adyacencia
            for item in nodoU.lista_vecinos:
                vecino = self.get_vertice(item)
                # Si el vecino no ha sido visitado, se cambian sus atributos y se encola
                if vecino.estado == "NO VISITADO":
                    vecino.estado = "VISITADO"
                    vecino.distancia = nodoU.distancia + 1
                    vecino.padre = nodoU.label
                    ColaQ.encolar(vecino)
        # Como resultado de BFS se imprimen los atributos de los nodos
        for item in self.lista_vertices:
            print("Nombre de Vertice: " + item.label)
            print("{}: {}".format(" Distancia al nodo raiz (nivel)", item.distancia))
            print("{}: {}".format(" Estado", item.estado))
            print("{}: {}".format(" Padre", item.padre))

    def DFS(self, root):
        """ Realiza una busqueda en profundidad dado un nodo raiz

        """

        self.ResetEstados()
        print("")
        print("Busqueda en profundidad con vertice raiz = " + root)
        print("A continuación se muestran todos los nodos alcanzables desde " + root)
        # Declaración de una lista como pila
        lista_stack = []
        # Se mete a la pila el nodo raíz de la busqueda
        lista_stack.append(root)
        # Mientras que la pila no esté vacía, se hace pop al último nodo agregado a la pila,
        # si no ha sido visitado se cambia e imprime su estado y se meten a la pila sus vecinos
        while lista_stack:
            nodo_etiqueta = lista_stack.pop()
            nodo = self.get_vertice(nodo_etiqueta)
            if nodo.estado == "NO VISITADO":
                nodo.estado = "VISITADO"
                print("Nodo " + nodo_etiqueta + " VISITADO")
                for vecino_label in nodo.lista_vecinos:
                    lista_stack.append(vecino_label)
            else:
                return print("Ciclo")

    def ResetEstados(self):
        """ Establece los atributos iniciales de estado, distancia y padre por defecto para todos
           los nodos en el grafo:

        """

        for nodo in self.lista_vertices:
            nodo.estado = "NO VISITADO"
            nodo.distancia = None
            nodo.padre = None

    def dijkstra(self, nodo_etiqueta, flag=1):
        """ Encuentra la ruta más corta a todos los nodos del grafo dado un vértice raíz, cuya
           etiqueta se proporciona como primer parametro, y se indica mandando un 0 como
           segundo parametro.
           La bandera (flag) es 1 por default para cuando se manda a llamar de manera recursiva

        """

        nodo = self.get_vertice(nodo_etiqueta)
        # Al comienzo, se usa una bandera para inicializar los atributos del nodo raíz
        # de forma que "padre" es un objeto nodo y no una etiqueta, y totalDistance
        # pasa de infinito a 0
        if flag == 0:
            nodo.padre = nodo
            nodo.totalDistance = 0
            flag = 1
            print("Nodo raíz sobre el que se hace dijkstra: " + nodo.label)
        else:
            print("Nodo sobre el que se hace dijkstra: " + nodo.label)
        # Iteración sobre el índice de los vecinos del nodo
        for i in range(len(nodo.lista_vecinos)):
            # Aquí v es una etiqueta del vecino [i]
            v = nodo.lista_vecinos[i]
            print(" Vecino : " + v)
            # Aquí v ya es un objeto vértice, vecino [i]
            v = self.get_vertice(v)
            # p es la distancia del nodo al vecino [i]
            p = nodo.lista_pesos[i]
            # Si la distancia actual que toma para llegar a ese vecino es mayor que la de
            # p + la distancia total (recorrido) del nodo que se está revisando, entonces
            # el nodo padre del vecino se cambia por el nodo actual, se actualiza la
            # distancia que toma llegar a él y se mete a la cola de prioridad
            print(" {} = {}".format("Distancia al vecino", p))
            print(" {} = {}".format("^ más recorrido que lleva el nodo", p + nodo.totalDistance))
            if v.totalDistance > p + nodo.totalDistance:
                v.padre = nodo
                print(" {} {} {} {}".format("Ahora el nodo", v.label, "tiene como padre a", nodo.label))
                v.totalDistance = p + nodo.totalDistance
                # Mete el nodo en la cola de prioridad, manteniendo la invariante del heap (dentro
                # del heap, cada nodo padre tiene un valor menor o igual que cualquiera de sus hijos)
                heappush(cola_prioridad, (v.totalDistance, v))
                for item in cola_prioridad:
                    print("     cola: nodo[" + item[1].label + "] , recorrido[" + str(item[0]) + "]")
        # Cuando termina de iterar sobre los vecinos, el estado cambia a VISITADO y
        # se extrae el peso y etiqueta del nodo más pequeño de la cola de prioridad (heap)
        nodo.estado = "VISITADO"
        (p, ne) = heappop(cola_prioridad)
        # Si el nodo extraído de la cola no se ha visitado, se hace dijkstra sobre él
        # de manera recursiva
        if ne.estado == "NO VISITADO":
            self.dijkstra(ne.label)

    def ruta(self, nodo_final_etiqueta):
        """ Devuelve el camino de nodos a seguir con la distancia más corta para llegar al nodo destino
           (que se pasa como atributo) dado el nodo inicial con el que se mandó llamar al método dijkstra
           anteriormente

        """
        # Se obtiene el objeto nodo (destino)
        nodo = self.get_vertice(nodo_final_etiqueta)
        # Se agrega la etiqueta del nodo destino a la lista que representa el camino más corto
        # a seguir
        distanciaMin = nodo.totalDistance
        etiquetas = [nodo_final_etiqueta]
        # Mientras que la etiqueta del nodo actual no sea igual a la etiqueta de su nodo padre
        # Recordando que el algoritmo dijkstra establece el padre de un nodo como el mejor nodo anterior
        # para llegar a él
        while nodo.label != nodo.padre.label:
            # El nodo actual se iguala a su nodo padre
            nodo = nodo.padre
            # Su etiqueta se agrega a la lista de etiquetas
            etiquetas.append(nodo.label)
        # Se invierte el orden de la lista
        etiquetas.reverse()
        return (print("{} {} {} {} {} {}".format("Camino más corto de nodos con distancia mínima de", distanciaMin,
                                                 "para llegar al nodo", nodo_final_etiqueta, ":", etiquetas)))

    def make_set(self, vertice):
        """ Establece el padre de un vértice como si mismo y su rank (rango en el grafo) como 0.

        """
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(self, vertice):
        """ Encuentra a cuál subconjunto o componente pertenece un nodo al seguir sus nodos padres hasta que un ciclo
            sea encontrado (un nodo cuyo padre es si mismo)

        """
        if parent[vertice] != vertice:
            parent[vertice] = self.find(parent[vertice])
        return parent[vertice]

    def union(self, vertice1, vertice2):
        """ Union por rank: unifica en un subconjunto a dos nodos al encontrar los nodos raíz de cada elemento,
        si estas raices son diferentes, convierte a una raíz en el padre del otro nodo tomando en cuenta el
        rank de cada raíz (añade el árbol más pequeño a la raíz del árbol más grande)

        """
        # Se guardará en las variables "root#" el nodo raíz del subconjunto al que pertenezca cada vértice
        root1 = self.find(vertice1)
        root2 = self.find(vertice2)
        # Compara si las raíces son diferentes
        if root1 != root2:
            # Si el rank de la raíz#1 es mayor al rank de la raíz#2, la raíz#1 se vuelve padre de la raíz#2
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            # De otra forma, la raíz#2 se vuelve padre de la raíz#1
            else:
                parent[root1] = root2
                # Si el rank de las raíces son iguales, el rank de la raíz#2 se incrementa en 1
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    def kruskal(self):
        """ Devuelve el arbol de expansión mínima en el grafo

        """
        # Inicializa el conjunto vacio que representa el árbol de expansión mínima
        minimum_spanning_tree = set()
        # Ordena las aristas por su distancia (de menor a mayor)
        self.edges.sort()
        for vertice in self.lista_vertices:
            # Se llama a make_set con cada vértice como parametro de la función
            self.make_set(vertice.label)
        for edge in self.edges:
            weight, vertice1, vertice2 = edge
            # Si los vértices pertenecen a conjuntos diferentes, se unifican y se agrega la arista al conjunto del
            # árbol de expansión mínima
            if self.find(vertice1) != self.find(vertice2):
                self.union(vertice1, vertice2)
                minimum_spanning_tree.add(edge)
        return sorted(minimum_spanning_tree)
