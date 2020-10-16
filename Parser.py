import json


def read_file():
    with open('input.json','r') as f:
        return json.loads(f.read())


def get_adjacency_matrix(works, edjes, count):
    arr = [[0 for i in range(count)] for j in range(count)]
    for i in edjes:
        arr[i['start']-1][i['finish']-1] = works[i['start']-1]['normal_len']
    return arr


def get_input_data():
    all_file = read_file()
    works = all_file['works']
    milestones = all_file['milestones']
    edjes = all_file['edjes']
    adj_matrix = get_adjacency_matrix(works, edjes, len(works) + len(edjes))
    return works, milestones, adj_matrix


if __name__ == '__main__':
    get_input_data()
