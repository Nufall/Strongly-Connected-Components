from typing import Iterator
from abc import ABC, abstractmethod, abstractproperty


class Graph(ABC):
    @abstractproperty
    def vertex_count(self) -> int:
        pass

    @abstractmethod
    def successors(self, vertex: int) -> Iterator[int]:
        pass

    @abstractmethod
    def transpose(self):
        pass

    def json(self):
        return {
            "vertices": self.vertex_count - 1,
            "edges": [
                [u, v] for u in range(self.vertex_count) for v in self.successors(u)
            ],
        }


class AdjacencyMatrix(Graph):
    adjacency_matrix: list[list[int]]

    def __init__(self, adjacency_matrix) -> None:
        self.adjacency_matrix = adjacency_matrix

    @staticmethod
    def parse(graph: dict) -> Graph:
        v, edges = graph["vertices"], graph["edges"]
        adjacency_matrix = [list() for _ in range(v + 1)]

        for i in range(v + 1):
            row = [False for _ in range(v + 1)]
            adjacency_matrix[i] = row

        for [src, dst] in edges:
            adjacency_matrix[src][dst] = True
        return AdjacencyMatrix(adjacency_matrix)

    def __str__(self) -> str:
        out = []
        n = len(self.adjacency_matrix)
        header = "".join(f"{i:2}" for i in range(n))
        out.append("  " + header)

        for i in range(n):
            row = ""
            for j in range(n):
                if self.adjacency_matrix[i][j]:
                    row += f"{1:2}"
                else:
                    row += f"{0:2}"
            out.append(f"{i:2}{row}")

        return "\n".join(out)

    @property
    def vertex_count(self) -> int:
        return len(self.adjacency_matrix)

    def successors(self, src: int) -> Iterator[int]:
        for dst in range(self.vertex_count):
            if self.adjacency_matrix[src][dst] and dst != src:
                yield dst

    def transpose(self):
        adjacency_matrix = [
            [False for _ in range(self.vertex_count)]
            for _ in range(self.vertex_count)
        ]

        for u in range(self.vertex_count):
            for v in range(self.vertex_count):
                adjacency_matrix[u][v] = self.adjacency_matrix[v][u]

        return AdjacencyMatrix(adjacency_matrix)


class AdjacencyList(Graph):
    adjacency_list: list[list[int]]

    def __init__(self, adjacency_list) -> None:
        self.adjacency_list = adjacency_list

    @staticmethod
    def parse(graph: dict) -> Graph:
        v, edges = graph["vertices"], graph["edges"]
        adjacency_list = [list() for _ in range(v + 1)]
        for [src, dst] in edges:
            adjacency_list[src].append(dst)

        for xs in adjacency_list:
            xs.sort()
        
        return AdjacencyList(adjacency_list)

    def __str__(self) -> str:
        out = []
        n = len(self.adjacency_list)
        for i in range(n):
            xs = self.adjacency_list[i]
            out.append(f"{i:2} -> {xs}")
        return "\n".join(out)

    @property
    def vertex_count(self) -> int:
        return len(self.adjacency_list)

    def successors(self, src: int) -> Iterator[int]:
        for dst in self.adjacency_list[src]:
            if dst != src:
                yield dst

    def transpose(self):
        adjacency_list = [list() for _ in range(self.vertex_count)]

        for u in range(self.vertex_count):
            for v in self.adjacency_list[u]:
                adjacency_list[v].append(u)

        return AdjacencyList(adjacency_list)
