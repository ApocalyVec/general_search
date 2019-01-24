# adapted from https://www.bogotobogo.com/python/python_graph_data_structures.php
import math


class Vertex:
    def __init__(self, node):
        self.id = node
        self.heuristic = math.inf  # the default heuristic is infinity
        self.connection = {}

    # def __init__(self, node, heuristic):  # initialize with heuristic
    #     self.id = node
    #     self.heuristic = heuristic  # the default heuristic is infinity
    #     self.connection = {}

    def __str__(self):  # used for the printing method
        return 'id: ' + str(self.id) + ' Heuristic: ' + str(self.heuristic) +\
               ' Connections: ' + str([x.id for x in self.connection])

    def __gt__(self, other):
        return self.id > self.id

    # def __getitem__(self, index):
    #     return self.id[index]

    # def __setitem__(self, index, value):
    #     self.bricks.bricksId[index] = value

    def get_id(self):
        return self.id

    def add_connection(self, vertex, weight=0):
        self.connection[vertex] = weight  # using the neighbor vertex as a key and the weight as its value

    def get_connection(self):
        return self.connection.keys()

    def get_weight(self, other_vertex):
        return self.connection[other_vertex]  # get the value designated by the other vertex as a key
