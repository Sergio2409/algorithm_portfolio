#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#
from collections import OrderedDict
from .linked_list import LinkedList


class Vertex(object):
    """Vertex graph representation.

    """
    def __init__(self, node, adjacent=None, level=None):
        self.node = node
        if(adjacent):
            self.adjacent = adjacent
        else:
            self.adjacent = {}
        self.level = level
        self.shortest_path = []

    def add_adjacent(self, vertex, weight=0):
        adjacentnts = self.adjacent.get(vertex, {})

        self.adjacent[vertex] = weight

    def __repr__(self):
        return str(self.node)
        

NoPathFound = object()


class Edge(list):

    def __init__(self, source, to, weight):
        self.source = source
        self.to = to
        self.weight = weight
        self.append(self.source)
        self.append(self.to)
        self.append(self.weight)


class Path(object):
    """Path of graph implementation

    """
    def __init__(self, graph, from_source):
        pass

    def has_path_to(self, vertex):
        '''Returns True if exists a path from `from_source` to 
        `vertex` passed otherwise returns False

        '''
        pass

    def path_to(self, vertex):
        """Return the path from `from_source` to `vertex` if exists
           otherwise returns `NoPathFound`
        """
        pass


class Graph(object):
    """

    """

    def __init__(self, edges):
        """
        Undirected Graph initializer
        :param edges: Edges of the graph must be passed as tuple pair for each edge, but if the edges has weight it
                      must be passed. Example: [[0,5], [2, 4], [2, 3], [1, 2], [0, 1], [3, 4], [3, 5], [0, 2]]

        """
        self.vertices = []
        self.edges = []
        self.marked = {}
        self._edges_count = 0
        self.adjacency = OrderedDict()

        for line in edges:
            vertex = line[0]
            adj_to_vertex = line[1]
            weight = 0
            if len(line) > 2:
                weigth = line[2]
            self.add_edge(vertex, adj_to_vertex, weight)
            if vertex not in self.vertices:
                self.vertices.append(vertex)
            if adj_to_vertex not in self.vertices:
                self.vertices.append(adj_to_vertex)

    @staticmethod
    def initialize_bag(v1, v2, weight=0):
        bag = LinkedList()
        bag.add(Edge(v1, v2, weight))
        return bag

    def add_edge(self, v1, v2, weight=0):
        """Add an edge to the grap

        :param v1: vertex 2
        :param v2: vertex 1
        :param weight: edge weight
        :return:None

        """
        self._edges_count += 1
        bag1 = self.adjacency.get(v1, None)
        bag2 = self.adjacency.get(v2, None)
        if bag1 is None:
            bag1 = self.initialize_bag(v1, v2, weight)
        else:
            bag1.add([v1, v2, weight])
        if bag2 is None:
            bag2 = self.initialize_bag(v1, v2, weight)
        else:
            bag2.add([v1, v2, weight])
        self.adjacency[v1] = bag1
        self.adjacency[v2] = bag2

    def adjacent(self, vertex):
        """
        Return a list of vertices adjacent to `vertex`.

        :param vertex:
        :return: Adjacency list for vertex if vertex exists otherwise raise an exception

        """
        adjacent = self.adjacency.get(vertex, None)
        if adjacent:
            return adjacent
        else:
            #print("Vertex {0} does not exists!".format(str(vertex)))
            return []

    def degree(self, vertex):
        """
        Returns the degree of the passed vertex

        :param vertex:
        :return: An integer representing the vertex degree

        """
        adjacent = self.adjacency.get(vertex, None)
        if adjacent:
            return adjacent.size
        else:
            raise Exception("Vertex {0} does not exists!".format(str(vertex)))

    @property
    def vertices_count(self):
        """
        Returns the number of vertex of the grap.
        :return: An integer representing the number of vertices of the graph.

        """
        return len(self.vertices)

    @property
    def edges_count(self):
        """
        Returns the number of edges of the grap.
        :return:

        """
        return self._edges_count

    def __str__(self):
        """
        String representation of the graph.
        :return:

        """
        pass


class DiGraph(Graph):
    """
    Directed Graph

    Set of vertices connected pairwise by directed edges.

    Digraph problems:

    + Shortest path. What is the shortest directed path from s to t ?
    + Topological sort. Can you draw a digraph so that all edges point upwards?
    + Strong connectivity. Is there a directed path between all pairs of vertices?
    + Transitive closure. For which vertices v and w is there a path from v to w ?
    + PageRank. What is the importance of a web page?


    Example:
    >>> graph = DiGraph([[4,2], [ 2, 3], [ 3,2 ], [ 6, 0], [ 0,1 ], [ 2,0 ], [ 11,12 ], [ 2, 9], [9, 10], [ 9, 11], [ 8, 9], [ 10,12 ], [ 11,4 ], [ 4,3 ], [ 3, 5], [6 , 8], [ 8,6 ], [ 5, 4], [0 , 5], [ 6,9 ], [ 7,6 ]])

    """

    def add_edge(self, v1, v2, weight=0):
        """Add an edge to the grap

        :param v1: vertex 2
        :param v2: vertex 1
        :param weight: edge weight
        :return:None

        """
        self._edges_count += 1
        bag1 = self.adjacency.get(v1, None)
        if bag1 is None:
            bag1 = self.initialize_bag(v1, v2, weight)
        else:
            bag1.add([v1, v2, weight])
        self.adjacency[v1] = bag1

    def reverse(self):
        """
        Return the reverse of this digraph
        :return:
        """
        raise NotImplemented("Not implemented")
