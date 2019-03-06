#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#
"""
Module description goes here

"""
from heapq import heappush, heappop
from collections import OrderedDict, deque
from algorithm import Algorithm


class GraphSearch(object):

    def __init__(self, graph, source):
        self.marked = OrderedDict()  # marked[v] = true if v connected to s
        self.edgeTo = OrderedDict()  # edgeTo[v] = previous vertex on path from s to v
        self.source = source
        self.graph = graph
        for vertex in graph.vertices:
            self.marked[vertex] = False

    def has_path_to(self, vertex):
        """
        Return true if exist a path to vertex `v` from `self.s`
        :param vertex:
        :return: True or False

        """
        return self.marked[vertex]

    def path_to(self, vertex):
        """
        Path from `source` to `vertex`; null if no such path
        :param vertex:
        :return:
        """
        _end = vertex
        path = []
        source_in_path = self.source in path
        while not source_in_path:
            new_vertex = self.edgeTo.get(vertex, None)
            if new_vertex is None:
                return []
            else:
                path.append(new_vertex._from)
                vertex = new_vertex._from
            source_in_path = self.source in path
        path.reverse()
        path.append(_end)
        return path


class DFS(Algorithm, GraphSearch):
    """
    Depth-first search algorithm

    Goal: Systematically search through a graph.
    Idea: Mimic maze exploration.

    Use example:
    from graph_search_algs import DFS
    from data_structures.graph import UndirectedGraph
    graph = UndirectedGraph([[0, 5], [4, 3], [0, 1], [9, 12], [6, 4], [5, 4], [0, 2], [11, 12], [9, 10], [0, 6], [7, 8], [9, 11], [5, 3]])
    paths = DFS(graph, 0)

    """

    def __init__(self, graph, source):
        super(DFS, self).__init__(graph, source)
        self.dfs(self.graph, self.source)

    def dfs(self, graph, vertex):
        """
        Find vertices connected to v
        :param graph:
        :param vertex:
        :return:
        """
        self.marked[vertex] = True
        for _node in graph.adjacent(vertex):
            new_vertex = _node.value[1]
            if not self.marked[new_vertex]:
                self.dfs(graph, new_vertex)
                self.edgeTo[new_vertex] = vertex

    @classmethod
    def info(cls):
        print('''

        Typical Applications:
        ・ Find all vertices conected to a given source vertex/
        ・Find a path between two vertices.

        Algorithm.
        ・ Use recursion (ball of string).
        ・ Mark each visited vertex (and keep track of edge taken to visit it).
        ・ Return (retrace steps) when no unvisited options.

        Data structures.
        ・ boolean[] marked to mark visited vertices.
        ・ int[] edgeTo to keep tree of paths.
        (edgeTo[w] == v) means that edge v-w taken to visit w for first time

        Proposition. 
        ・ DFS marks all vertices connected to s in time proportional to the sum of their degrees.

        Pf. [correctness]
        ・ If w marked, then w connected to s (why?)
        ・ If w connected to s, then w marked.
           (if w unmarked, then consider last edge
           on a path from s to w that goes from a
           marked vertex to an unmarked one).

        Pf. [running time]
        ・ Each vertex connected to s is visited once.

        After DFS, can find vertices connected to s in constant time and can find a path to s 
        (if one exists) in time proportional to its length.

        ''')


class BFS(Algorithm, GraphSearch):
    """
    Breadth-first search algorithm

    Goal: Systematically search through a graph.
    Idea: Shortest path. Find path from s to t that uses fewest number of edges.

    Use example:
    from graph_search_algs import BFS
    from data_structures.graph import UndirectedGraph
    graph = UndirectedGraph([[0,5], [2, 4], [2, 3], [1, 2], [0, 1], [3, 4], [3, 5], [0, 2]])
    paths = BFS(graph, 0)

    """

    def __init__(self, graph, source):
        super(BFS, self).__init__(graph, source)
        self.bfs(self.graph, self.source)

    def bfs(self, graph, vertex):
        """
        Find vertices connected to v
        :param graph:
        :param vertex:
        :return:
        """
        queue = deque([vertex])
        self.marked[vertex] = True

        while len(queue) > 0:
            from_vertex = queue.popleft()
            for _node in graph.adjacent(from_vertex):
                new_vertex = _node.value[1]
                if not self.marked[new_vertex]:
                    queue.append(new_vertex)
                    self.marked[new_vertex] = True
                    self.edgeTo[new_vertex] = from_vertex

    @classmethod
    def info(cls):
        print('''
        
        Breadth-first search. Put unvisited vertices on a queue.
        
        Goal.
        Shortest path. Find path from s to t that uses fewest number of edges.
        
        Intuition. 
        ・ BFS examines vertices in increasing distance from s.
        
        Pf. [correctness] 
        ・ Queue always consists of zero or more vertices of distance k from s, followed by zero or more vertices of 
           distance k + 1.
        
        Pf. [running time]
        ・ Each vertex connected to s is visited once.
        
        
        Typical Applications:
        ・ Fewest number of hops in a communication network.
        ・ Kevin Bacon numbers
        ・ Erdös numbers
        
        Algorithm.
        BFS (from source vertex s)
        Put s onto a FIFO queue, and mark s as visited.
        Repeat until the queue is empty:
        - remove the least recently added vertex v
        - add each of v's unvisited neighbors to the queue, and mark them as visited.
        
        Data structures.
        ・ boolean[] marked to mark visited vertices.
        ・ int[] edgeTo to keep tree of paths.
        (edgeTo[w] == v) means that edge v-w taken to visit w for first time
                
        Proposition. 
        ・ BFS computes shortest paths (fewest number of edges) from s to all other vertices in a graph in time 
           proportional to E + V.
        
        After BFS, can find vertices connected to s in constant time and can find a path to s 
        (if one exists) in time proportional to its length.
        
        ''')


class ConnectedComponent(Algorithm):
    """
    Depth-first search algorithm

    Goal: Partition vertices into connected components.

    Idea: .

    """

    @classmethod
    def info(cls):
        print('''
        Definitions.
        ・ Vertices v and w are connected if there is a path between them.
        ・ A connected component is a maximal set of connected vertices.
        
        The relation "is connected to" is an equivalence relation:
        ・ Reflexive: v is connected to v.
        ・ Symmetric: if v is connected to w, then w is connected to v.
        ・ Transitive: if v connected to w and w connected to x, then v connected to x.
        
        Remark. 
        ・ Given connected components, can answer queries in constant time.
        
        Goal.
        ・ Preprocess graph to answer queries of the form is v connected to w? in constant time.
        
        Algorithm.
        Connected components
        ・ Initialize all vertices v as unmarked.
        ・ For each unmarked vertex v, run DFS to identify all vertices discovered as part of the same component.
        
         Typical Applications:
        ・ Particle detection. Given grayscale image of particles, identify "blobs."
        ・ Particle tracking. Track moving particles over time.        
        
        ''')


class Dijkstra(Algorithm, GraphSearch):
    """
    Example:

    from data_structures.graph import DiGraph
    from graph_search_algs import Dijkstra
    graph = DiGraph([[0, 1, 5], [0, 7, 8], [0, 4, 9], [1 , 3, 15], [1, 2, 12], [1, 7, 4], [2, 3, 3], [2, 6, 11], [3, 6, 9], [4, 7, 5], [4, 5, 4], [4, 6, 20], [5, 2, 1], [5, 6, 13], [7, 2, 7], [7, 5, 6]])
    shortest_path = Dijkstra(graph, 0)

    """

    def __init__(self, graph, source):
        """

        :param graph:
        :param source:
        """
        super(Dijkstra, self).__init__(graph, source)
        self.distTo = OrderedDict()  # edgeTo[v] = previous vertex on path from s to v
        self.ordered_queue = []
        self.source = source
        self.graph = graph
        BIG_INT = 100000
        for vertex in graph.vertices:
            self.distTo[vertex] = BIG_INT

        self.distTo[source] = 0
        heappush(self.ordered_queue, [0.0, source])
        while len(self.ordered_queue) > 0:
            _, vertex = heappop(self.ordered_queue)  # Take the vertex with the minimum weight.
            self.marked[vertex] = True
            for node in graph.adjacent(vertex):
                self.relax_edge(node.value)

    def relax_edge(self, edge):
        """

        :param edge:
        :return:
        """
        v = edge._from
        w = edge.to
        if self.distTo[w] > self.distTo[v] + edge.weight:
            self.distTo[w] = self.distTo[v] + edge.weight
            self.edgeTo[w] = edge
            if w not in self.ordered_queue:
                heappush(self.ordered_queue, [self.distTo[w], w])

    @classmethod
    def info(cls):
        print('''
        Dijkstra's algorithm
        
        ・ Consider vertices in increasing order of distance from s (non-tree vertex with the lowest distTo[] value).
        ・ Add vertex to tree and relax all edges pointing from that vertex.
        
        Proposition. 
        ・ Dijkstra's algorithm computes a SPT in any edge-weighted digraph with nonnegative weights.
        
        Pf.
        ・ Each edge e = v → w is relaxed exactly once (when v is relaxed), leaving distTo[w] ≤ distTo[v] + e.weight().
        ・ Inequality holds until algorithm terminates because:
            – distTo[w] cannot increase.
            – distTo[v] will not change
        ・ Thus, upon termination, shortest-paths optimality conditions hold.
        
        Dijkstra’s algorithm seem familiar?
        ・ Prim’s algorithm is essentially the same algorithm.
        ・ Both are in a family of algorithms that compute a graph’s spanning tree.        
        
        ''')