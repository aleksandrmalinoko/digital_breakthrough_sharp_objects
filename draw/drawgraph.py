import plotly.express as px
import pandas as pd

import matplotlib.pyplot as plt
import networkx as nx


def test(temp, sum):

    '''
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Old", Text="Length: 20 days <br> Cost: 50.000"),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Old", Text="Length: 10 days <br> Cost: 50.000"),
        dict(Task="Job C", Start='2019-02-20', Finish='2019-05-30', Resource="New", Text="Length: 25 days <br> Cost: 50.000"),
        dict(Task="Job D", Start='2009-02-20', Finish='2009-05-30', Resource="New", Text="Length: 30 days <br> Cost: 50.000"),
        dict(Task="Job E", Start='2010-02-20 00:00:01', Finish='2010-02-20 23:59:59', Resource="New", Text="Length: 5 days <br> Cost: 50.000"),
        dict(Task="Job F", Start='2014-02-20', Finish='2014-05-30', Resource="New", Text="Length: 2 day <br> Cost: 60.000")
    ])
    '''

    fig = px.timeline(temp, x_start="start", x_end="end", y="name", color="status", title="Потрачено средств: " + str(sum))
    fig.update_yaxes(autorange="reversed")
    fig.show()


def draw_graph(dg):
    plt.subplot(121)
    nx.draw(dg, with_labels=True, font_weight='bold')
    plt.show()
