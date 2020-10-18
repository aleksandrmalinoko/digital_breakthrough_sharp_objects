import os.path
from parsing import parser
from draw import drawgraph
from graph.Data_pandas import *


def main(inputFile, editFile, date, maxPrice):
    if os.path.isfile(inputFile) is False:
        return
    if os.path.isfile(editFile) is False:
        return

    works, milestones_input, adj_matrix = parser.get_input_data(inputFile)

    DG_frame_input = build_frame(works + milestones_input)
    milestones_frame_input = build_frame(milestones_input)

    works, milestones = parser.get_edit_data(editFile)

    DG_frame_edit = build_frame(works + milestones)
    milestones_frame_edit = build_frame(milestones)

    DG_frame_input = was_edited(DG_frame_input, DG_frame_edit)

    DG = nx.DiGraph()
    DG.add_weighted_edges_from(adj_matrix)

    sum, DG_frame_input = calculate_shift(DG_frame_input, DG_frame_edit, date, DG)


    for i in milestones_input:
        DG_frame_input["start"][i["uid"]] = DG_frame_input["start"][i["uid"]] + " 00:00:01"
        DG_frame_input["end"][i["uid"]] = DG_frame_input["end"][i["uid"]] + " 23:59:59"

    drawgraph.test(DG_frame_input, sum)
