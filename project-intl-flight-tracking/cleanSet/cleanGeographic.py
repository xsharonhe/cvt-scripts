import pandas as pd
import numpy as np

def cleanGeographic(file):
    """
    :param file(file) of the inserted dataframe
    """
    df = pd.read_csv(file, skiprows=1)
    df.drop(df.tail(2).index, inplace=True)
    df.index = df['Year']
    df = df.T


    df.drop(index=[df.index[0], df.index[1], df.index[2],
                  df.index[3],df.index[5],
                  df.index[7]], inplace=True)
    df = df.T
    df['Quarter'] = df.rename(columns={'Quarter': 'Quarter('}, inplace=True)
    df = df.T
    df['Location'] = df.index.str.split('(').str[0]
    df.drop(index='Quarter', inplace=True)

    return df

