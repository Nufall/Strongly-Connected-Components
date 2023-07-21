import time
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from tarjan import tarjan
from generate_graphs import generate_graph

from graph import AdjacencyList, AdjacencyMatrix, Graph
from kosarajus import kosaraju
from path_based import path_based

LIST_MIN_V = 500
LIST_MAX_V = 1500

MAT_MIN_V = 200
MAT_MAX_V = 400

MAX_REPS = 1
k = 10**9


def bench_adj_alg(algorithm):
    adj_list_times = []
    for v in range(LIST_MIN_V, LIST_MAX_V):
        times = []

        for _ in range(MAX_REPS):
            graph = generate_graph(v=v)
            graph = AdjacencyList.parse(graph)

            before = time.time() * k
            _ = algorithm(graph)
            after = time.time() * k

            times.append(after - before)

        adj_list_times.append((np.median(times)))
    return adj_list_times


def bench_mat_alg(algorithm):
    adj_mat_times = []
    for v in range(MAT_MIN_V, MAT_MAX_V):
        times = []

        for _ in range(MAX_REPS):
            graph = generate_graph(v=v)
            graph = AdjacencyMatrix.parse(graph)
            before = time.time() * k
            _ = algorithm(graph)
            after = time.time() * k
            times.append(after - before)

        adj_mat_times.append((np.median(times)))

    return adj_mat_times


if __name__ == "__main__":
    K_adj_list = bench_adj_alg(kosaraju)
    K_adj_mat = bench_mat_alg(kosaraju)

    T_adj_list = bench_adj_alg(tarjan)
    T_adj_mat = bench_mat_alg(tarjan)

    P_adj_list = bench_adj_alg(path_based)
    P_adj_mat = bench_mat_alg(path_based)
    # t_adj_list, t_adj_mat = bench_alg(tarjan)
    # p_adj_list, p_adj_mat = bench_alg(path_based)

    #print(k_adj_list)
    #print(k_adj_mat)
    #plt.title("k_adj_list")

    figure, axis = plt.subplots(3,2)
    figure.set_figwidth(20)
   # figure.set_figheight(7)
    figure.suptitle('SCC Algorithm')
    

    axis[0,0].plot(range(LIST_MIN_V, LIST_MAX_V), K_adj_list)
    axis[0,0].set_title("Transposal Adjacency List")

    axis[0,1].plot(range(MAT_MIN_V, MAT_MAX_V), K_adj_mat)
    axis[0,1].set_title("Transposal Adjacency Matrix")

    axis[1,0].plot(range(LIST_MIN_V, LIST_MAX_V), T_adj_list)
    axis[1,0].set_title("Tarjan Adjacency List")

    axis[1,1].plot(range(MAT_MIN_V, MAT_MAX_V), T_adj_mat)
    axis[1,1].set_title("Tarjan Adjacency Matrix")

    axis[2,0].plot(range(LIST_MIN_V, LIST_MAX_V), P_adj_list)
    axis[2,0].set_title("Path Based Adjacency List")

    axis[2,1].plot(range(MAT_MIN_V, MAT_MAX_V), P_adj_mat)
    axis[2,1].set_title("Path Based Adjacency Matrix")
    plt.show()
    # plt.yt
    # plt.plot(range(LIST_MIN_V, LIST_MAX_V), k_adj_list)
    # plt.show()
    # plt.title('t_adj_list')
    # plt.plot(range(LIST_MIN_V, LIST_MAX_V), t_adj_list)
    # plt.show()
    # plt.title('p_adj_list')
    # plt.plot(range(MIN_V, MAX_V), p_adj_list)
    # plt.show()
    # plt.title('k_adj_mat')
    # plt.plot(range(MIN_V, MAX_V), k_adj_mat)
    # plt.show()
    # plt.title('t_adj_mat')
    # plt.plot(range(MIN_V, MAX_V), t_adj_mat)
    # plt.show()
    # plt.title('p_adj_mat')
    # plt.plot(range(MIN_V, MAX_V), p_adj_mat)
    # plt.show()
