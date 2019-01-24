def dfs_expand(nodes, graph, queue, visited):
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
                    temp = nodes[:]  # do not apply the insert change to the original varibale
                    temp.insert(0, n)
                    queue.push(temp)
