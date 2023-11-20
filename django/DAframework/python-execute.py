import json
import plotly.graph_objects as go

songs = ['Balls to the Wall', 'Inject The Venom', 'Snowballed', 'Overdose', 'Deuces Are Wild', 'Not The Doctor', 'Por Causa De Você', 'Welcome Home (Sanitarium)', 'Snowblind', 'Cornucopia']
counts = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

fig = go.Figure([go.Bar(x=songs, y=counts)])
fig.update_layout(title_text='Song Counts', xaxis_title='Song Name', yaxis_title='Count')
print(fig.to_json())