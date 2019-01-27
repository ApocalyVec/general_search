import os
import time


from Graph import Graph
from Queue import Queue
from Expand import dfs_expand, bfs_expand, dls_expand

depth = 0 # depth limit used by IDDFS

def general_search(graph, search_method, d):

    start = time.time()

    print("Running: " + search_method)
    if search_method == 'IDDFS':
        print("L = " + str(d) + "     Expanded     Queue")
    else:
        print("         Expanded     Queue")
    queue = Queue()
    root = g.get_vertex('S')
    destination = g.get_vertex('G')

    queue.push([root])


    while 1:
        nodes = queue.get_left_peek()  # get the left peek without popping

        # use the given search method
        # DFS
        if search_method == 'DFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dfs_expand(graph, queue)
        # BFS
        elif search_method == 'BFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            bfs_expand(graph, queue)

        elif search_method == "DLS":
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dls_expand(graph, queue, 2)

        elif search_method == 'IDDFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dls_expand(graph, queue, d)

        if nodes[0] == destination:
            end = time.time()
            print("         goal reached! " + "Time taken by " + search_method + " is", end - start, "seconds")
            return nodes[0]

        if queue.isEmpty():
            if search_method == 'IDDFS':
                d = d + 1
                general_search(g, 'IDDFS', d)  # use recursion for IDDFS

            # print("No solution, terminated")
            return


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


general_search(g, 'DFS', depth)
general_search(g, 'BFS', depth)
general_search(g, 'DLS', depth)  # change the depth limitation with dls_expand call, dl = 2
general_search(g, 'IDDFS', depth)

# g.add_vertex('a')
# g.add_edge('a', 'b', 7)
# g.set_heuristic_for_vertex('a', 10)


