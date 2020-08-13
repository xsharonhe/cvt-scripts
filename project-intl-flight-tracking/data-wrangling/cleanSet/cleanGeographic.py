def cleanGeographic(file):i
    """
    cleans geographic text form bts .xls format
    :param file name
    """
    df = pd.read_csv(file, skiprows=1)
    df.drop(df.tail(2).index, inplace=True)
    df['Period('] = df['Year'].astype(str) + ' - ' + df['Quarter'].astype(str).str[0]
    df.index = df['Period(']
    df = df.T


    df.drop(index=[df.index[0], df.index[1], df.index[2],
                  df.index[3], df.index[4],
                  df.index[6], df.index[8]], inplace=True)
    df = df.T
    df['Quarter'] = df.rename(columns={'Quarter': 'Quarter('}, inplace=True)
    df = df.T
    df['Location'] = df.index.str.split('(').str[0]
    df.drop(index='Quarter', inplace=True)

    df = df.T
    df.index = df.index.astype(str)
    for n in range(1, 5):
        df = df.drop(index=['1995 - {}'.format(n), '1996 - {}'.format(n), '1997 - {}'.format(n),
                        '1998 - {}'.format(n), '1999 - {}'.format(n),
                           '2000 - {}'.format(n), '2001 - {}'.format(n),
                           '2002 - {}'.format(n), '2003 - {}'.format(n),
                           '2004 - {}'.format(n), '2005 - {}'.format(n),
                           '2006 - {}'.format(n), '2007 - {}'.format(n),
                           '2008 - {}'.format(n), '2009 - {}'.format(n)])

    return df

