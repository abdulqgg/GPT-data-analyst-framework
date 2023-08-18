import json
import plotly.graph_objects as go

names = ['Luís', 'Leonie', 'François', 'Bjørn', 'František']
ages = [38, 38, 38, 38, 38]

fig = go.Figure(data=go.Scatter(x=names, y=ages, mode='markers'))

fig.update_layout(title='Data Visualization',
                  xaxis_title='Names',
                  yaxis_title='Ages')

print(fig.to_json())