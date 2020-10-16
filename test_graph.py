import networkx as nx

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
print(list(DG.successors(1)))
print(list(DG.neighbors(1)))
