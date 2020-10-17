import networkx as nx
from parsing.parser import get_input_data, get_edit_data
from graph.traversal import find_source_vertex, find_stock_vertex, remove_input_edges, partitioning_graph
# from draw.drawgraph import draw_graph
from view.window import Window
from tkinter import Tk


if __name__ == "__main__":
    root = Tk()
    root.geometry("350x100+300+300")
    app = Window()
    root.mainloop()


'''import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed")
fig.show()'''


'''
main()
DG = nx.DiGraph()
works, milestones, adj_matrix = get_input_data()
DG.add_weighted_edges_from(adj_matrix)

# y = find_stock_vertex(DG)
# x = find_source_vertex(DG)

DG.nodes()

test = partitioning_graph(DG, milestones)

draw_graph(DG)
'''
'''try:
    print(nx.dijkstra_path(DG, 1, 3))
except nx.exception.NetworkXNoPath:
    print("kek")'''


# test = remove_input_edges(DG, 2)
# draw_graph(test)

# sub_graph = DG.remove_node(x)
# print(DG.nodes())
'''
draw_graph(DG)
sub_graph = DG.subgraph([1, 2, 3])
draw_graph(sub_graph)
'''

'''for i in DG.nodes():
    print(i)
    print(list(DG.neighbors(i)))
    for j in list(DG.neighbors(i)):
        print(DG[i][j])
'''
# print(DG.nodes)
# print(DG.adjacency())

# print(list(DG.neighbors(0)))
# draw_graph(DG)

'''
Example for get edit data:
works, milestones = get_edit_data()

Example for edit data - in edit.json
'''
