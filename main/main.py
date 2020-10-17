import os.path
from parsing import parser
from draw import drawgraph
import networkx as nx


def main(inputFile, editFile, date, maxPrice):
    if os.path.isfile(inputFile) is False:
        return
    if os.path.isfile(editFile) is False:
        return

    works, milestones, adj_matrix = parser.get_input_data(inputFile)

    '''print(parser.get_input_data(inputFile))
    print("-----------------")
    print(parser.get_edit_data(editFile))'''

    drawgraph.test()

    DG = nx.DiGraph()
    # works, milestones, adj_matrix = get_input_data()
    DG.add_weighted_edges_from(adj_matrix)

    # y = find_stock_vertex(DG)
    # x = find_source_vertex(DG)
    drawgraph.draw_graph(DG)
    # DG.nodes()

    # test = partitioning_graph(DG, milestones)


    '''works, milestones, adj_matrix = parser.get_input_data(inputFile)
    worksEdit, milestonesEdit = parser.get_edit_data(editFile)'''
