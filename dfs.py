print("DEPTH FIRST SEARCH")
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A'],
         'D': ['A'],
         'E': ['B'],
         'F': ['B']
         }


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
    print(levels)
    return path


print(dfs(graph, 'A', 'F'))
