import os.path
from parsing import parser
from draw import drawgraph
from graph import Data_pandas
import networkx as nx
from graph.Data_pandas import *


def main(inputFile, editFile, date, maxPrice):
    if os.path.isfile(inputFile) is False:
        return
    if os.path.isfile(editFile) is False:
        return

    works, milestones_input, adj_matrix = parser.get_input_data(inputFile)

    DG_frame_input = build_frame(works + milestones_input)
    milestones_frame_input = build_frame(milestones_input)

    # print(DG_frame_input)
    works, milestones = parser.get_edit_data(editFile)

    DG_frame_edit = build_frame(works + milestones)
    milestones_frame_edit = build_frame(milestones)

    DG_frame_input, DG_frame_edit = was_edited(DG_frame_input, DG_frame_edit)

    temp = Data_pandas.build_frame(works + milestones)
    print(temp)
    for i in milestones:
        temp["start"][i["uid"]] = temp["start"][i["uid"]] + " 00:00:01"
        # temp["end"][i["uid"]] = temp["end"][i["uid"]] + " 23:59:59"
    print("---------------------------------------")
    print(temp)
    # print(temp["start"][1])

    drawgraph.test(temp)

    '''print(parser.get_input_data(inputFile))
    print("-----------------")
    print(parser.get_edit_data(editFile))'''

    # drawgraph.test()

    # DG = nx.DiGraph()
    # works, milestones, adj_matrix = get_input_data()
    # DG.add_weighted_edges_from(adj_matrix)

    # y = find_stock_vertex(DG)
    # x = find_source_vertex(DG)
    # drawgraph.draw_graph(DG)
    # DG.nodes()

    # test = partitioning_graph(DG, milestones)


    '''works, milestones, adj_matrix = parser.get_input_data(inputFile)
    worksEdit, milestonesEdit = parser.get_edit_data(editFile)'''
