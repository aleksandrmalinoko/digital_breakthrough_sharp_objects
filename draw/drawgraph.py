import plotly.express as px


def test(temp, sum, maxPrice, date):
    temp['Text'] = str()
    for i in list(temp['uid']):
        if temp['status'][i] is "edited":
            temp['Text'][i] = f"Length: {temp['normal_len'][i]} days <br> Cost: {temp['replan_cost'][i]}"
        else:
            temp['Text'][i] = f"Length: {temp['normal_len'][i]} days"
    fig = px.timeline(temp, x_start="start", x_end="end", y="name", color="status", title="Потрачено средств: "
                        + str(sum) + "<br>Максимальное кол-во средств: " + str(maxPrice)
                        + "<br>Дата изменений: " + str(date), text="Text")
    fig.update_yaxes(autorange="reversed")
    fig.add_shape(
        type='line',
        line_color='gold',
        line_width=3,
        opacity=1,
        line_dash='dot',
        x0=date,
        x1=str(date) + " 01:00:00",
        xref='x',
        y0=0,
        y1=len(list(temp['uid']))-1,
        yref='y')
    fig.add_annotation(text='Дата изменений', xanchor='right', x=date, arrowhead=1, showarrow=True)
    fig.show()
