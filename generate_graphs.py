import os
import json
from random import randint

MAX_GRAPHS: int = 500
MAX_VERTEX_COUNT: int = 10
MAX_EDGE_COUNT: int = 2 * MAX_VERTEX_COUNT


def generate_graph(v: int = MAX_GRAPHS, e: int = MAX_EDGE_COUNT):
    vertex_count = randint(1, v)
    edge_count = randint(1, e)

    edges = set()
    for _ in range(edge_count):
        src = randint(0, vertex_count)
        dst = randint(0, vertex_count)
        edges.add((src, dst))
    edges = list(edges)

    return {
        "vertices": vertex_count,
        "edges": edges,
    }


if __name__ == "__main__":
    if os.path.isdir("tests"):
        os.system('RMDIR "tests" /S /Q')
    os.mkdir("tests")

    for i in range(0, MAX_GRAPHS):
        outpath = os.path.join("tests", f"{i}.json")
        graph = generate_graph()
        with open(outpath, "w") as file:
            json.dump(graph, file, indent=4)
