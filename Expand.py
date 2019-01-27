def dfs_expand(graph, queue):
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


def dls_expand(graph, queue, dl):  # dl = depth limit, a integer number
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


def bfs_expand(graph, queue):
    nodes = queue.pop()
    node_to_be_expanded = nodes[0]

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

        # for i in connections:
            # print("Connection is: ")
            # print(i)

    for c in connections:
        if c not in nodes:
            temp = nodes[:]  # do not apply the insert change to the original varible
            temp.insert(0, c)
            queue.push_right(temp)

    # visited.append(node_to_be_expanded)
        # print("Queue after pushing is: ")
            # print(queue)


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
