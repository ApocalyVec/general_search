import copy
from Path import Path
from Heap import Heap

def dfs_expand(queue):
    nodes = queue.pop()
    # if nodes[0] not in visited:  # do nothing is n is already visited
        # print("visiting: ")
        # print(nodes[0].id)

    connections = nodes[0].get_connection()
    connections = list(connections)

    # print("before sorting")
    # for n in connections:
    #     print(n.id)

    connections.sort(key=lambda x: x.id, reverse=True)

    # print("after sorting")
    # print(connections)
    # for n in connections:
    #     print(n.id)

    for n in connections:
            # print("in the for loop: ")
            # print(n.id)
            if n not in nodes:  # ndoes is equivalent to a visited (explored) list
                temp = nodes[:]  # do not apply the insert change to the original varible
                temp.insert(0, n)
                queue.push(temp)


def dls_expand(queue, dl):  # dl = depth limit, a integer number
    nodes = queue.pop()

    if len(nodes) > dl:  # return if the depth limit is hit
        return
    # if nodes[0] not in visited:

    connections = nodes[0].get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=True)

    for n in connections:
        if n not in nodes:
            temp = nodes[:]
            temp.insert(0, n)
            queue.push(temp)


def bfs_expand(queue):
    nodes = queue.pop()
    node_to_be_expanded = nodes[0]

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

        # for i in connections:
            # print("Connection is: ")
            # print(i)

    for c in connections:
        if c not in nodes:  # because node in 'nodes' are 'visited'
            temp = nodes[:]  # do not apply the insert change to the original varible
            temp.insert(0, c)
            queue.push_right(temp)

    # visited.append(node_to_be_expanded)
        # print("Queue after pushing is: ")
            # print(queue)


def ucs_expand(heap):
    path = heap.pop()
    nodes = path.get_vertexes()
    # nodes.reverse()  # must reverse for the new path to work
    node_to_be_expanded = path.get_end()

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

    for c in connections:
        if c not in nodes:  # because node in 'nodes' are 'visited'

            new_path = Path()

            for n in nodes:
                # print("adding to new path: " + n.id)
                new_path.add_vertex(n)

            new_path.add_vertex(c)
            heap.push(new_path)


def gs_expand(heap):
    path = heap.pop()
    nodes = path.get_vertexes()
    # nodes.reverse()  # must reverse for the new path to work
    node_to_be_expanded = path.get_end()

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

    for c in connections:
        if c not in nodes:  # because node in 'nodes' are 'visited'

            new_path = Path()

            for n in nodes:
                # print("adding to new path: " + n.id)
                new_path.add_vertex(n)

            new_path.add_vertex(c)
            heap.push_heuristic(new_path)


def as_expand(heap):
    path = heap.pop()
    nodes = path.get_vertexes()
    # nodes.reverse()  # must reverse for the new path to work
    node_to_be_expanded = path.get_end()

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

    for c in connections:
        if c not in nodes:  # because node in 'nodes' are 'visited'

            new_path = Path()

            for n in nodes:
                # print("adding to new path: " + n.id)
                new_path.add_vertex(n)

            new_path.add_vertex(c)
            heap.push_a_star(new_path)


def hc_expand(heap):

    path = heap.pop()
    nodes = path.get_vertexes()
    # nodes.reverse()  # must reverse for the new path to work
    node_to_be_expanded = path.get_end()

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

    for c in connections:
        if c not in nodes:  # because node in 'nodes' are 'visited'

            new_path = Path()

            for n in nodes:
                # print("adding to new path: " + n.id)
                new_path.add_vertex(n)

            new_path.add_vertex(c)
            heap.push_hc(new_path)

    heap.hc_sort()  # find whether path to explore next after pushing all children


def bms_expand(heap, beam_width, visited):


    if heap.size() > beam_width:
        # print("Before trimming: "+ heap.str_heuristic())

        # heap.heuristic_sort()
        heap.trim(beam_width)

        # print("After trimming: " + heap.str_heuristic())

    path = heap.pop()



    nodes = path.get_vertexes()
    # nodes.reverse()  # must reverse for the new path to work
    node_to_be_expanded = path.get_end()

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

    for c in connections:
        if c not in nodes and c not in visited:  # because node in 'nodes' are 'visited'

            new_path = Path()

            for n in nodes:
                # print("adding to new path: " + n.id)
                new_path.add_vertex(n)

            new_path.add_vertex(c)
            heap.push_bms(new_path)  # use the same push as HC (simple insertion)



# def iddfs_expand(graph, queue, depth):
#     nodes = queue.pop()
#
#     if len(nodes) > depth:  # return if the depth limit is hit
#         return
#     # if nodes[0] not in visited:
#
#     connections = nodes[0].get_connection()
#     connections = list(connections)
#     connections.sort(key=lambda x: x.id, reverse=True)
#
#     for n in connections:
#         if n not in nodes:
#             temp = nodes[:]
#             temp.insert(0, n)
#             queue.push(temp)
