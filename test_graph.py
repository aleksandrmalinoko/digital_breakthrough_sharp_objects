import networkx as nx
from parsing.parser import get_input_data, get_edit_data
from draw.drawgraph import draw_graph


DG = nx.DiGraph()
works, milestones, adj_matrix = get_input_data()
DG.add_weighted_edges_from(adj_matrix)
print(list(DG.neighbors(0)))
draw_graph(DG)

'''
Example for get edit data:
works, milestones = get_edit_data()

Example for edit data - in edit.json
'''
