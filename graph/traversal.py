import networkx as nx


def find_source_vertex(graph: nx.DiGraph):
    vertex = 0
    for i in range(graph.number_of_nodes()):
        flag = True
        for j in range(graph.number_of_nodes()):
            if i in graph.neighbors(j):
                flag = False
                break
        if flag is True:
            vertex = i
    return vertex


def remove_input_edges(graph: nx.DiGraph, vertex: int):
    for i in range(graph.number_of_nodes()):
        if vertex in graph.neighbors(i):
            graph.remove_edge(i, vertex)
    return graph


def find_stock_vertex(graph: nx.DiGraph):
    vertex = 0
    for i in range(graph.number_of_nodes()):
        if len(list(graph.neighbors(i))) == 0:
            vertex = i
    return vertex


def partitioning_graph(graph: nx.DiGraph, milestones):
    subgraphs = {}
    for i in list(graph.nodes()):
        mile = 0
        for j in milestones:
            if i == j["uid"]:
                break
        for j in milestones:
            try:
                temp = nx.dijkstra_path(graph, i, j["uid"])
                for k in milestones:
                    if j != k and k in temp:
                        temp = nx.dijkstra_path(graph, i, k["uid"])
                        mile = k["uid"]
            except nx.exception.NetworkXNoPath:
                pass
        if mile in subgraphs:
            subgraphs[mile].append(i)
        else:
            subgraphs[mile] = [i]
    print(subgraphs)
    return subgraphs
