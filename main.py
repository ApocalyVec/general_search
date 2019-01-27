import os
import time


from Graph import Graph
from Queue import Queue
from Path import Path
from Heap import Heap
from Expand import dfs_expand, bfs_expand, dls_expand, ucs_expand, gs_expand, as_expand, hc_expand

depth = 0 # depth limit used by IDDFS


def General_Search(graph, search_method, d):

    start = time.time()

    print("Running: " + search_method)
    if search_method == 'IDDFS':
        print("L = " + str(d) + "     Expanded     Queue")
    else:
        print("         Expanded     Queue")

    root = g.get_vertex('S')
    destination = g.get_vertex('G')

    # queue for unweighted search
    queue = Queue()
    queue.push([root])

    #heap for weighted search
    path = Path()
    path.add_vertex(root)
    heap = Heap()
    heap.push(path)

    while 1:

        if search_method == 'UCS' or search_method == 'GS' or search_method == 'AS'\
                or search_method == 'HC' or search_method == 'BMS':
            nodes = heap.get_left_peek().get_vertexes()
            nodes.reverse()
        else:
            nodes = queue.get_left_peek()  # get the left peek without popping

        # use the given search method
        # DFS
        if search_method == 'DFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dfs_expand(queue)
        # BFS
        elif search_method == 'BFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            bfs_expand(queue)

        elif search_method == "DLS":
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dls_expand(queue, 2)

        elif search_method == 'IDDFS':
            print('         ' + nodes[0].id, end='              ')
            print(queue)
            dls_expand(queue, d)

        elif search_method == 'UCS':
            print('         ' + nodes[0].id, end='              ')
            print(heap)
            ucs_expand(heap)

        elif search_method == 'GS':
            print('         ' + nodes[0].id, end='              ')
            print(heap.str_heuristic())
            gs_expand(heap)

        elif search_method == 'AS':
            print('         ' + nodes[0].id, end='              ')
            print(heap.str_a_star())
            as_expand(heap)

        elif search_method == 'HC':
            # if len(nodes) > 1:
            #     unexplored_children = list(nodes[0].get_connection())
            #     unexplored_children.remove(nodes[1])
            #
            #     # print(unexplored_children)
            #
            #     if len(unexplored_children) != 0: # there is unvisited node(s) from this node
            #         print('         ' + nodes[0].id, end='              ')
            #         print(heap.str_heuristic())  # use the same on as the Greedy Search
            #
            #         hc_expand(heap)
            #
            # else:
            print('         ' + nodes[0].id, end='              ')
            print(heap.str_heuristic())  # use the same on as the Greedy Search

            hc_expand(heap)

        elif search_method == 'BMS':
            print('a')


        # must be in this order: check destination before searching
        # otherwise IDDFS won't work
        if nodes[0] == destination:
            end = time.time()
            print("         goal reached! " + "Time taken by " + search_method + " is", end - start, "seconds")
            return nodes[0]

        if queue.isEmpty() or heap.isEmpty():
            if search_method == 'IDDFS':
                d = d + 1
                General_Search(g, 'IDDFS', d)  # use recursion for IDDFS

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
            g.add_edge(arguments[0], arguments[1], arguments[2].rstrip())  # use strip to remove any newline characters
            # print("section 1: " + line)
        elif current_section == 2:
            arguments = line.split(" ")
            g.set_heuristic_for_vertex(arguments[0], arguments[1].rstrip())
            # print("section 2: " + line)

# IMPORTANT: set the ending destination's heuristic to be 0
# Also the starting node is always S and the destination is G
g.set_heuristic_for_vertex('G', 0)

print("Graph read from file: ")
g.print_all_vertices()
input("Press Enter to continue...")


General_Search(g, 'DFS', depth)
General_Search(g, 'BFS', depth)
General_Search(g, 'DLS', depth)  # change the depth limitation with dls_expand call, dl = 2
General_Search(g, 'IDDFS', depth)
General_Search(g, 'UCS', depth)
General_Search(g, 'GS', depth)
General_Search(g, 'AS', depth)
General_Search(g, 'HC', depth)
General_Search(g, 'BMS', depth)


# p1 = Path()
# p1.add_vertex(g.get_vertex('S'))
# p1.add_vertex(g.get_vertex('A'))
# # p1.add_vertex(g.get_vertex('B'))
# print(p1)
#
#
# p2 = Path()
# p2.add_vertex(g.get_vertex('S'))
# p2.add_vertex(g.get_vertex('A'))
# p2.add_vertex(g.get_vertex('D'))
# p2.add_vertex(g.get_vertex('E'))
# print(p2)
#
# p3 = Path()
# p3.add_vertex(g.get_vertex('S'))
# p3.add_vertex(g.get_vertex('A'))
# p3.add_vertex(g.get_vertex('D'))
# p3.add_vertex(g.get_vertex('E'))
# p3.add_vertex(g.get_vertex('F'))
# p3.add_vertex(g.get_vertex('G'))
# print(p3)
#
# p3 = Path()
# p3.add_vertex(g.get_vertex('S'))
# p3.add_vertex(g.get_vertex('A'))
# p3.add_vertex(g.get_vertex('D'))
# p3.add_vertex(g.get_vertex('E'))
# p3.add_vertex(g.get_vertex('F'))
# p3.add_vertex(g.get_vertex('G'))
# print(p3)
#
# h = Heap()
#
# h.push(p3)
#
# h.push(p2)
#
# h.push(p1)
#
# print(h)
#
# print('Popping: ')
# while not h.isEmpty():
#     print(h.pop())

# w = g.get_vertex('A').get_weight(g.get_vertex('S'))





