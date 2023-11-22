import json
import plotly.express as px
import pandas as pd

data = {'Song': ['The Trooper', 'Untitled', 'The Number Of The Beast', 'Sure Know Something', 'Hallowed Be Thy Name', 
                 'Eruption', 'Where Eagles Dare', 'Welcome Home (Sanitarium)', 'Sweetest Thing', 'Surrender'],
        'Rating': [5, 4, 4, 4, 4, 4, 3, 3, 3, 3]}

df = pd.DataFrame(data)

fig = px.bar(df, x='Song', y='Rating')
fig.update_layout(title='Song Ratings')
print(fig.to_json())