def dfs_expand(nodes, graph, queue, visited):
    connections = nodes[0].get_connection()

    # print("before sorting")
    # for n in connections:
    #     print(n.id)
    #
    # list(connections).sort()
    #
    # print("after sorting")

    for n in connections:
        print(n.id)

    for n in connections:
        if n not in visited: # do nothing is n is already visited
            visited.append(n)
            temp = nodes[:]  # do not apply the insert change to the original varibale
            temp.insert(0, n)
            queue.push(temp)