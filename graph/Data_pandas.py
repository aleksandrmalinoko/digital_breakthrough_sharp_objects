import pandas as pd
import networkx as nx
from datetime import datetime, timedelta


def date_calculate(start, leng):
    return datetime.strftime(datetime.strptime(start, '%Y-%m-%d') + timedelta(int(leng)), '%Y-%m-%d')


def date_minus(start, end):
    return (datetime.strptime(end, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')).days



def build_frame(data_list):
    ls = list()
    for i in range(len(data_list)):
        ls.append(data_list[i]['uid'])
    data_frame = pd.DataFrame(data_list, index=ls)
    data_frame['end'] = 0
    data_frame['replan_cost'] = 0
    data_frame['status'] = "planned"
    for i in ls:
        data_frame['end'][i] = date_calculate(data_frame['start'][i], data_frame['normal_len'][i])
            #datetime.strftime(datetime.strptime(data_frame['start'][i], '%Y-%m-%d') + timedelta(int(data_frame['normal_len'][i])), '%Y-%m-%d')
    return data_frame


def was_edited(planned, fact):
    for i in fact['uid']:
        planned['status'][i] = "edited"
        planned['start'][i] = fact['start'][i]
        planned['normal_len'][i] = fact['normal_len'][i]
    return planned


def calculate_shift(planned, fact, data, graph:nx.DiGraph):
    sum = 0
    for i in fact['uid']:
        if datetime.strptime(planned['start'][i], '%Y-%m-%d') < datetime.strptime(data, '%Y-%m-%d'):
            planned['end'][i] = date_calculate(planned['start'][i], planned['normal_len'][i])
        else:
            neighbors_list = list(graph.neighbors(i))
            flag = True

            for j in neighbors_list:
                if date_calculate(planned['start'][i], planned['normal_len'][i]) > planned['start'][j]:
                    flag = False
                    if planned['normal_len'][i] > planned['min_len'][i]:
                        tmp = planned['normal_len'][i] - planned['min_len'][i]
                        if date_calculate(planned['start'][j], tmp) >= date_calculate(planned['start'][i], planned['normal_len'][i]):
                            sum = (planned['normal_len'][i] - date_minus(planned['start'][j], planned['start'][i])) * planned['shift_before'][i]
                            planned['normal_len'][i] = date_minus(planned['start'][j], planned['start'][i])
                            planned['end'][i] = planned['start'][j]
                            planned['replan_cost'][i] += sum
                    pass
            if flag is True:
                planned['end'][i] = date_calculate(planned['start'][i], planned['normal_len'][i])
    return sum, planned