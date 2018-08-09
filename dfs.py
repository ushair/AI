print("DEPTH FIRST SEARCH")
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A'],
         'D': ['A'],
         'E': ['B'],
         'F': ['B']
         }


def dfs(graph, start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)
    return path


print(dfs(graph, 'A'))
