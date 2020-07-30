import seaborn as sns

def timeSeriesEda(set_name, title, col_name):
    """
    Performs time series preliminary analysis using seaborn lineplots.
    :param set_name: name of dataframe (dataframe),
    :param title: title of graph (str),
    :param col_name: name of column in dataframe (str)
    """

    sns.set(style="darkgrid",rc={'figure.figsize':(25,15)})

    ax = sns.lineplot(x=set_name.index, y=set_name[col_name].astype(float))

    plt.title(title)

    fig_1 = ax.get_figure()

    return fig_1
