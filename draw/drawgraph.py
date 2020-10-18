import plotly.express as px


def test(temp, sum):
    temp['Text'] = str()
    for i in list(temp['uid']):
        if temp['status'][i] is "edited":
            temp['Text'][i] = f"Length: {temp['normal_len'][i]} days <br> Cost: {temp['replan_cost'][i]}"
        else:
            temp['Text'][i] = f"Length: {temp['normal_len'][i]} days"
    fig = px.timeline(temp, x_start="start", x_end="end", y="name", color="status", title="Потрачено средств: " + str(sum), text="Text")
    fig.update_yaxes(autorange="reversed")
    fig.show()
