import plotly.graph_objects as go
import pandas as pd
from io import StringIO

data = """Name,Surname,Count,Score
Helena,Holý,7,49.620000000000005
Hugh,O'Reilly,7,45.62000000000001
Ladislav,Kovács,7,45.62000000000001
Luis,Rojas,7,46.62000000000002
Richard,Cunningham,7,47.62000000000002
"""

# create a dataframe
df = pd.read_csv(StringIO(data))

fig = go.Figure([go.Bar(x=df['Name'], y=df['Score'])])
fig.update_layout(title_text='Score by Name')
fig.show()
