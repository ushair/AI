graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A'],
         'D': ['A'],
         'E': ['B'],
         'F': ['B']
         }


def bfs(graph, start, goal):
    explored = []
    queue = [start]

    levels = {}
    levels[start] = 0

    visited = [start]
    while queue:
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour] = levels[node]+1
                if neighbour is goal:
                    print("Goal Found :- "+neighbour)
                    break

    print("LEVELS:- ")
    print(levels)
    print("PATH:- ")
    return explored


def dfs(graph, start, goal):
    levels = {}
    levels[start] = 0
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        if v is goal:
            print("GOAL FOUND :- " + v)
            break
        for w in reversed(graph[v]):
            if w not in path:
                levels[w] = levels[v]+1
                stack.append(w)
    print("LEVELS:- ")
    print(levels)
    print("PATH:- ")
    return path


print("DEPTH FIRST SEARCH :- ")
print(dfs(graph, 'A', 'F'))
print("BREADTH FIRST SEARCH :- ")
print(bfs(graph, 'A', 'F'))
