# adapted from https://www.bogotobogo.com/python/python_graph_data_structures.php
from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_dic = {}
        self.size = 0

    def __iter__(self):
        return iter(self.vertex_dic.values())  # return a list for iterating through

    def add_vertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertex_dic[vertex] = new_vertex
        self.size = self.size + 1
        return new_vertex

    # def add_vertex_heuristic(self, vertex, heuristic): # add vertex with heuristic
    #     new_vertex = Vertex(vertex, heuristic)
    #     self.all_vertices[vertex] = new_vertex
    #     self.size = self.size + 1
    #     return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_dic:
            return self.vertex_dic[n]
        else:
            return None

    def add_edge(self, start, end, weight=0):
        if start not in self.vertex_dic:
            self.add_vertex(start)  # add the starting vertex if it is not in the graph
        if end not in self.vertex_dic:
            self.add_vertex(end)  # add the ending vertex if it is not in the graph

        self.vertex_dic[start].add_connection(self.vertex_dic[end], weight)
        self.vertex_dic[end].add_connection(self.vertex_dic[start], weight)

    def get_all_vertices(self):
        return self.vertex_dic.keys()

    # def get_vertex_by_id(self, id):
    #     for v in self.all_vertices:
    #         if v.id == id:
    #             return v
    #     # if the vertex with the given if is not found
    #     raise RuntimeError('vertex with id: ' + id + " not found")

    def set_heuristic_for_vertex(self, vertex, heuristic):
        if vertex not in self.vertex_dic:
            raise RuntimeError('vertex with id: ' + vertex + " not found")
        else:
            self.vertex_dic[vertex].heuristic = heuristic

    def print_all_vertices(self):
        for vertex in self:
            print(vertex)

    # all the serach methods

