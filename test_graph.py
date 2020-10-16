import matplotlib.pyplot as plt

import networkx as nx
import json


def read_file():
    with open('input.json', 'r') as f:
        return json.loads(f.read())


def get_adjacency_matrix(works, edjes):
    arr = list()
    for i in edjes:
        arr.append(tuple((i['start']-1, i['finish']-1, works[i['start']-1]['normal_len'])))
    return arr


def get_input_data():
    all_file = read_file()
    return all_file['works'], all_file['milestones'], get_adjacency_matrix(all_file['works'], all_file['edjes'])


DG = nx.DiGraph()
works, milestones, adj_matrix = get_input_data()
DG.add_weighted_edges_from(adj_matrix)
# DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
# print(list(DG.successors(0)))
print(list(DG.neighbors(0)))
plt.subplot(121)
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()
