import networkx as nx
from parsing.parser import get_input_data, get_edit_data
from graph.traversal import find_source_vertex, find_stock_vertex
from draw.drawgraph import draw_graph


DG = nx.DiGraph()
works, milestones, adj_matrix = get_input_data()
DG.add_weighted_edges_from(adj_matrix)

find_stock_vertex(DG)
x = find_source_vertex(DG)
print(x)
for i in range(0, DG.number_of_nodes()):
    print(i)
    print(list(DG.neighbors(i)))

# print(DG.nodes)
# print(DG.adjacency())

# print(list(DG.neighbors(0)))
draw_graph(DG)

'''
Example for get edit data:
works, milestones = get_edit_data()

Example for edit data - in edit.json
'''
