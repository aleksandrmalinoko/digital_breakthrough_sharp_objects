import pandas as pd


def build_frame(data_list):
    ls = list()
    for i in range(len(data_list)):
        ls.append(data_list[i]['uid'])
    data_frame = pd.DataFrame(data_list, index=ls)
    return data_frame
