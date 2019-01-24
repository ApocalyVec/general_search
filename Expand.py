def dfs_expand(graph, queue, visited):
    nodes = queue.pop()
    if nodes[0] not in visited:  # do nothing is n is already visited
        # print("visiting: ")
        # print(nodes[0].id)
        visited.append(nodes[0])
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
                if n not in visited:
                    temp = nodes[:]  # do not apply the insert change to the original varible
                    temp.insert(0, n)
                    queue.push(temp)


def bfs_expand(graph, queue, visited):
    nodes = queue.pop()
    node_to_be_expanded = nodes[0]

    # if node_to_be_expanded not in visited:
    visited.clear()
    visited.extend(nodes)

    connections = node_to_be_expanded.get_connection()
    connections = list(connections)
    connections.sort(key=lambda x: x.id, reverse=False)

        # for i in connections:
            # print("Connection is: ")
            # print(i)

    for c in connections:
        if c not in visited:
            temp = nodes[:]  # do not apply the insert change to the original varible
            temp.insert(0, c)
            queue.push_right(temp)

    # visited.append(node_to_be_expanded)
        # print("Queue after pushing is: ")
            # print(queue)