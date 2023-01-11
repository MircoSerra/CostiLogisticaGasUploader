import pandas as pd
import KTE_artesian as kta
import datetime as dt
from dateutil.relativedelta import *

def quarter_to_datetime(x):
    q = x.split(' ')[0]
    year = x.split(' ')[1]
    date = dt.datetime.strptime(year, '%y') + relativedelta(months=(int(q[1]) * 3) - 3)
    return date

def genera_date_in_range(start, end):
    daterange = pd.date_range(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), freq='1M')
    daterange = daterange.union([daterange[-1] + relativedelta(months=1)])
    daterange = [(d - dt.timedelta(d.day - 1)) for d in daterange[1:-1]]
    return daterange

def update_costi_logistica_gas(path):
    df = pd.read_excel(path,
                       sheet_name='variabili gas', usecols='I:T', skiprows=2, nrows=20)
    #print('arr')
    df['Data'] = df.apply(lambda x: quarter_to_datetime(x['Quarter']), axis=1)
    df.set_index('Data', inplace=True)

    dict_of_dict_to_artesian = dict()
    for column in list(df.columns)[2:]:
        dict_of_dict_to_artesian[column] = kta.make_artesian_dict_actual(pd.DataFrame(df[column].fillna(0)), column)

    for k in list(dict_of_dict_to_artesian.keys()):
        for k_2 in list(dict_of_dict_to_artesian[k].keys()):
            months_between = genera_date_in_range(k_2, k_2 + relativedelta(months=3))
            for month in months_between:
                dict_of_dict_to_artesian[k][month] = dict_of_dict_to_artesian[k][k_2]

    for k in list(dict_of_dict_to_artesian.keys())[:-1]:
        kta.post_artesian_actual_time_series(dict_of_dict_to_artesian[k], dict(), 'DevKtE',
                                             'Componenti tariffari gas ' + k,
                                             'M')
    kta.post_artesian_actual_time_series(dict_of_dict_to_artesian['Spread contratto'], dict(), 'DevKtE',
                                         'UP_CETSERVOLA_1 spread contratto gas', 'M')
