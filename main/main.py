import os.path
from parsing import parser
from draw import drawgraph


def main(inputFile, editFile, date, maxPrice):
    if os.path.isfile(inputFile) is False:
        return
    if os.path.isfile(editFile) is False:
        return

    print(parser.get_input_data(inputFile))
    print("-----------------")
    print(parser.get_edit_data(editFile))

    drawgraph.test()


    '''works, milestones, adj_matrix = parser.get_input_data(inputFile)
    worksEdit, milestonesEdit = parser.get_edit_data(editFile)'''
