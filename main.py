import json
import os
import sys
from tarjan import tarjan
from kosarajus import kosaraju
from graph import AdjacencyList, AdjacencyMatrix
from path_based import path_based
from visualize import visualize


def same_elems(xs: list[list[int]], ys: list[list[int]]):
    return sorted([sorted(x) for x in xs]) == sorted([sorted(y) for y in ys])


if __name__ == "__main__":
    # testcase = sys.argv[1]
    # with open(f"./tests/{testcase}.json", "r") as file:
    #     graph_repr = json.load(file)
    #     graph_1 = AdjacencyList(graph_repr)
    #     graph_2 = AdjacencyMatrix(graph_repr)
    # scc_1 = Kosaraju(graph_1)
    #     print(f'scc_1={scc_1}')
    # scc_2 = Kosaraju(graph_2)
    #     print(f'scc_2={scc_2}')

     for testcase in os.listdir("./tests")[0:20]:
        #testcase = "5.json"
        testpath = os.path.join("tests", testcase)
        with open(testpath, "r") as file:
            graph_repr = json.load(file)

            adj_list = AdjacencyList.parse(graph_repr)
            adj_mat = AdjacencyMatrix.parse(graph_repr)
            
            adj_list_kosaraju = kosaraju(adj_list)
            adj_list_path_based = path_based(adj_list)

            adj_matrix_kosaraju = kosaraju(adj_mat)
            adj_matrix_path_based = path_based(adj_mat)

            adj_list_tarjan = tarjan(adj_list)
            adj_matrix_tarjan = tarjan(adj_mat)
           
            for x in [
                adj_list_kosaraju,
                adj_matrix_kosaraju,
                adj_list_path_based,
                adj_matrix_path_based,
                adj_list_tarjan,
                adj_matrix_tarjan,
            ]:
                for y in x:
                    y.sort()

            error = False

            all = [
                adj_list_kosaraju,
                adj_matrix_kosaraju,
                adj_list_path_based,
                adj_matrix_path_based,
                adj_list_tarjan,
                adj_matrix_tarjan,
            ]
            visualize(graph_repr,adj_list_kosaraju)
            # for i in range(1, len(all)):
            #     if not same_elems(all[i], all[i - 1]):
            #         error = True
            #         break

            # if error:
            #visualize(graph_repr, components=adj_list_kosaraju)
                # print(f"{adj_list_kosaraju=}")
                # print(f"{adj_list_path_based=}")
                # print(f"{adj_matrix_kosaraju=}")
                # print(f"{adj_matrix_path_based=}")
                # print(f"{adj_list_tarjan=}")
                # print(f"{adj_matrix_tarjan=}")
                # input()
