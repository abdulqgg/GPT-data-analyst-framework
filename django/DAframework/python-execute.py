import json
import plotly.graph_objects as go
import pandas as pd

data = {'Song': ['The Trooper', 'Untitled', 'The Number Of The Beast', 'Sure Know Something',
                 'Hallowed Be Thy Name', 'Eruption', 'Where Eagles Dare', 
                 'Welcome Home (Sanitarium)', 'Sweetest Thing', 'Surrender'],
        'Rating': [5, 4, 4, 4, 4, 4, 3, 3, 3, 3]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Table(header=dict(values=df.columns),
                               cells=dict(values=[df.Song, df.Rating]))])

print(fig.to_json())