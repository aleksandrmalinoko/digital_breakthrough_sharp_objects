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


def calculate_shift(planned, fact:pd.DataFrame, date, graph:nx.DiGraph):
    sum = 0
    # print(fact)
    # print("-----------")
    # fact.loc[4] = planned[4]
    # fact.loc[works[i]['uid']] = list(milestones[i]['uid'], milestones[i]['name'])
    # fact.append(list(planned.index))

    # copy
    # fact.loc[planned.index[5]] = planned.iloc[5]
    # sort
    planned = planned.sort_index()
    fact.sort_index()
    while fact.empty is not True:
        # get index
        # print(fact.index[0])
        idx = fact.index[0]
        # delete 0ed elem
        fact = fact.drop(fact.index[0])

        # Если конец ДО линии.
        if datetime.strptime(date_calculate(planned['start'][idx], planned['normal_len'][idx]), '%Y-%m-%d') < datetime.strptime(date, '%Y-%m-%d'):
            planned['end'][idx] = date_calculate(planned['start'][idx], planned['normal_len'][idx])
        # ИНАЧЕ
        else:
            # Берем потомков
            neighbors_list = list(graph.neighbors(idx))

            # Если начало ДО линии, а конец - ПОСЛЕ
            if planned['start'][idx] < date:
                # Проходим по всем потомкам
                for j in neighbors_list:
                    # Новый конец задачи
                    finish = date_calculate(planned['start'][idx], planned['normal_len'][idx])
                    # Если пересечение
                    if finish > planned['start'][j]:
                        # находим сдвиг старта
                        count = date_minus(planned['start'][j], finish)
                        # новый старт
                        planned["start"][j] = date_calculate(planned['start'][idx], planned['normal_len'][idx])
                        planned["status"][j] = "edited"
                        sum += count * planned["shift_later"][j]
                        planned['replan_cost'][j] += count * planned["shift_later"][j]
                        fact.loc[planned.index[j]] = planned.iloc[j]
                    planned['end'][idx] = finish
            # Если начало ПОСЛЕ линии
            else:
                for j in neighbors_list:
                    # Если не пересекается
                    if date_calculate(planned['start'][idx], planned['normal_len'][idx]) <= planned['start'][j]:
                        pass
                    else:
                        # Если старт + норм_лен > старта соседа
                        finish = date_calculate(planned['start'][idx], planned['normal_len'][idx])
                        # Если старт + мин_лен <= старта соседа
                        if date_calculate(planned['start'][idx], planned['min_len'][idx]) <= planned['start'][j]:
                            count = date_minus(planned['start'][j], finish)
                            sum += count * planned["time_cost"][idx]
                            planned['replan_cost'][idx] += count * planned["time_cost"][idx]
                            planned['normal_len'][idx] -= count
                            planned['end'][idx] = date_calculate(planned['start'][idx], planned['normal_len'][idx])
                        else:
                            # Если старт + мин_лен > старта соседа
                            # finish_min = date_calculate(planned['start'][idx], planned['min_len'][idx])
                            # изменения в старом
                            count = planned['normal_len'][idx] - planned['min_len'][idx]
                            sum += count * planned["time_cost"][idx]
                            planned['replan_cost'][idx] += count * planned["time_cost"][idx]
                            planned['normal_len'][idx] = planned['min_len'][idx]
                            planned['end'][idx] = date_calculate(planned['start'][idx], planned['normal_len'][idx])
                            # изменение в потомке
                            planned['start'][j] = planned['end'][idx]
                            planned['replan_cost'][j] += count * planned["shift_later"][j]
                            sum += count * planned["shift_later"][j]
                            planned['status'][j] = "edited"
                            fact.loc[planned.index[j]] = planned.iloc[j]
    return sum, planned

    '''
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
                            sum = (planned['normal_len'][i] - date_minus(planned['start'][i], planned['start'][j])) * planned['shift_before'][i]
                            planned['normal_len'][i] = date_minus(planned['start'][i], planned['start'][j])
                            planned['end'][i] = planned['start'][j]
                            planned['replan_cost'][i] += sum
                    pass
            if flag is True:
                planned['end'][i] = date_calculate(planned['start'][i], planned['normal_len'][i])
    return sum, planned
    '''