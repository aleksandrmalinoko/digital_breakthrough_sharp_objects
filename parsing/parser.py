import json


def read_file(path_file):
    with open(path_file, 'r') as f:
        return json.loads(f.read())


def get_adjacency_matrix(works, edges):
    arr = list()
    for i in edges:
        if i['start'] >= len(works):
            arr.append(tuple((i['start'], i['finish'], 0)))
        else:
            arr.append(tuple((i['start'], i['finish'], works[i['start']]['normal_len'])))
    return arr


def get_input_data(fileName):
    all_file = read_file(fileName)
    works = all_file['works']
    milestones = all_file['milestones']
    edges = all_file['edges']
    adj_matrix = get_adjacency_matrix(works, edges)
    return works, milestones, adj_matrix


def get_edit_data(fileName):
    all_file = read_file(fileName)
    works = all_file['works']
    milestones = all_file['milestones']
    return works, milestones
