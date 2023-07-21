from graph import Graph


def path_based(graph: Graph):
    c = 0
    n = graph.vertex_count
    components = []
    visited = [False] * n
    assigned = [False] * n
    preorder = [-1] * n
    s, p = [], []

    def visit(v: int):

        nonlocal c
        if visited[v]:
            return
        visited[v] = True
        preorder[v] = c
        c += 1

        #print(f'V = {v}:')
        s.append(v)
        p.append(v)


        #print(f'{s=}')
        #print(f'{p=}')

        for w in graph.successors(v):
            if preorder[w] == -1:
                #print(f'\tVisiting {w} from {v}')
                visit(w)
            elif not assigned[w]:
                #print(f'\tNode {w} was not assigned. {p=}')
                while len(p) > 0 and preorder[p[-1]] > preorder[w]:
                    #print(f'{preorder[p[-1]]=} > {preorder[w]=} ?; {p=}')
                    p.pop()

        if v == p[-1]:
            assigned[v] = True
            components.append([v])
            # TODO: Check
            while s[-1] != v:
                w = s.pop()
                assigned[w] = True
                components[-1].append(w)
            s.pop()
            p.pop()

    for v in range(n):
        if preorder[v] == -1:
            visit(v)

    return components
