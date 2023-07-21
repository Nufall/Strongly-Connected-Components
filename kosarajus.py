from graph import Graph

def kosaraju(graph: Graph) -> list[list[int]]:
    L = []
    components = []
    visited = [False] * graph.vertex_count
    assigned = [False] * graph.vertex_count
    transposed = graph.transpose()

    def assign(u: int, root: int):
        if assigned[u]: return

        assigned[u] = True

        if u == root:
            components.append([u])
        else:
            components[-1].append(u)


        for v in transposed.successors(u):
            assign(v, root)            

    def visit(u: int):
        if not visited[u]:
            visited[u] = True
    
            for v in graph.successors(u):
                visit(v)

            L.append(u)
    
    for u in range(graph.vertex_count):
        visit(u)

    while len(L) > 0:
        k = L.pop()
        assign(k, k)
    
    return components







    