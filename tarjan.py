import math
from graph import Graph


def tarjan(graph: Graph):
    count = 0
    seen = []
    components = []
    ids = [-1] * graph.vertex_count
    on_stack = [False] * graph.vertex_count
    low_link_number = [-1] * graph.vertex_count

    def visit(v: int):
        nonlocal count
        ids[v] = count
        low_link_number[v] = ids[v]
        count += 1

        seen.append(v)
        on_stack[v] = True

        for w in graph.successors(v):
            if ids[w] == -1:
                visit(w)

            if on_stack[w]:
                low_link_number[v] = min(
                    low_link_number[v],
                    low_link_number[w],
                )

        if ids[v] == low_link_number[v]:    
            components.append([v])
            while seen[-1] != v:
                w = seen.pop()
                on_stack[w] = False
                components[-1].append(w)
            seen.pop()
            on_stack[v] = False

    for v in range(graph.vertex_count):
        if ids[v] == -1:
            visit(v)

    return components