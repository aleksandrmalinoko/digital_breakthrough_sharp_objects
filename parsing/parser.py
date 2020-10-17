import json


def read_file(path_file):
    with open(path_file, 'r') as f:
        return json.loads(f.read())


def get_adjacency_matrix(works, edges):
    arr = list()
    for i in edges:
        if i['start']-1 >= len(works):
            arr.append(tuple((i['start'] - 1, i['finish'] - 1, 0)))
        else:
            arr.append(tuple((i['start']-1, i['finish']-1, works[i['start']-1]['normal_len'])))
    return arr


def get_input_data():
    all_file = read_file('input.json')
    works = all_file['works']
    milestones = all_file['milestones']
    edges = all_file['edges']
    adj_matrix = get_adjacency_matrix(works, edges)
    return works, milestones, adj_matrix


def get_edit_data():
    all_file = read_file('edit.json')
    works = all_file['works']
    milestones = all_file['milestones']
    return works, milestones
