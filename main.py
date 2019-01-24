import os
import time


from Graph import Graph
from Queue import Queue
from Expand import dfs_expand, bfs_expand


def general_search(graph, search_method):

    start = time.time()

    print("Running: " + search_method)
    print("     Expanded     Queue")
    queue = Queue()
    root = g.get_vertex('S')
    destination = g.get_vertex('G')

    queue.push([root])
    # print(queue)

    #
    # queue.push([Vertex('g'), Vertex('d')])
    # print(queue)
    # print(queue.state())

    visited = []

    while 1:
        if queue.empty():
            print("No solution, terminated")
            return

        nodes = queue.get_left_peek()  # get the left peek without popping

        # sort nodes by its ID alphabetically
        # print("before sorting")
        # for n in nodes:
        #     print(n.id)
        #
        # nodes.sort()
        #
        # print("after sorting")
        # for n in nodes:
        #     print(n.id)

        # use the given search method
        # DFS
        if search_method == 'DFS':
            print('     ' + nodes[0].id, end='              ')
            print(queue)
            dfs_expand(graph, queue, visited)
        # BFS
        elif search_method == 'BFS':
            print('     ' + nodes[0].id, end='              ')
            print(queue)
            bfs_expand(graph, queue, visited)

        if nodes[0] == destination:
            end = time.time()
            print("     goal reached! " + "Time taken by " + search_method + " is       ", end - start, "seconds")

            return nodes[0]


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


general_search(g, 'DFS')
general_search(g, 'BFS')


# g.add_vertex('a')
# g.add_edge('a', 'b', 7)
# g.set_heuristic_for_vertex('a', 10)


