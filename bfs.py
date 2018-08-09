print("Breadth First Search :- ")
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A'],
         'D': ['A'],
         'E': ['B'],
         'F': ['B']
         }


# visits all the nodes of a graph (connected component) using BFS
def bfs(graph, start, key):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start] = 0    # depth of start node is 0

    visited = [start]  # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be checked
    while queue:  # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour] = levels[node]+1
                if neighbour is key:
                    print("Goal Found "+neighbour)
                    break

    print(levels)

    return explored


ans = bfs(graph, 'A', 'F')
print(ans)
