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


def find_stock_vertex(graph: nx.DiGraph):
    vertex = 0
    for i in range(graph.number_of_nodes()):
        if len(list(graph.neighbors(i))) == 0:
            vertex = i
    return vertex
