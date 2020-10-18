
from parsing.parser import get_input_data, get_edit_data
from graph.traversal import find_source_vertex, find_stock_vertex
from draw.drawgraph import draw_graph
from graph.Data_pandas import *


DG = nx.DiGraph()
works, milestones, adj_matrix = get_input_data('input.json')
DG.add_weighted_edges_from(adj_matrix)

DG_frame_input = build_frame(works+milestones)
milestones_frame_input = build_frame(milestones)

print(DG_frame_input)
works, milestones = get_edit_data('edit.json')

DG_frame_edit = build_frame(works+milestones)
milestones_frame_edit = build_frame(milestones)

DG_frame_input = was_edited(DG_frame_input, DG_frame_edit)



print(DG_frame_input)

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
