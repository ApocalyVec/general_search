import os

from Graph import Graph
from Vertex import Vertex
from Queue import Queue

# def dfs_expand()

def general_search(graph, search_method):
    if search_method == 'BFS':
        print("Running BFS")
        queue = Queue()
        # queue.push([Vertex('s')])
        # queue.push([Vertex('g'), Vertex('d')])
        # print(queue)
        while 1:
            if queue.empty():
                print("No solution, terminated")
                return

            visiting_node = queue.pop()



filePath = str(input("Please enter a file path... Then press enter... "
                     "(Please note the Program will NOT validate the input file)"))
print(filePath)
assert os.path.exists(filePath), "File not found at " + filePath + ", Exiting..."

# creating graph from file
g = Graph()
current_section = 1;
with open(filePath) as input_file:
    for line in input_file:
        if line == "#####\n":
            current_section = 2;
            # print("start reading of section 2")
        elif current_section == 1:
            arguments = line.split(" ")
            g.add_edge(arguments[0], arguments[1], arguments[2])
            # print("section 1: " + line)
        elif current_section == 2:
            arguments = line.split(" ")
            g.set_heuristic_for_vertex(arguments[0], arguments[1])
            # print("section 2: " + line)

# IMPORTANT: set the ending destination's heuristic to be 0
# Also the starting node is always S and the destination is G
g.set_heuristic_for_vertex('G', 0)

print("Graph read from file: ")
g.print_all_vertices()
input("Press Enter to continue...")

general_search(g, 'BFS')

# g.add_vertex('a')
# g.add_edge('a', 'b', 7)
# g.set_heuristic_for_vertex('a', 10)


