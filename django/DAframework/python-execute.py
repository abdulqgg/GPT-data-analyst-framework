import json
import plotly.express as px

data = {
    'Song': ['The Trooper', 'Untitled', 'The Number Of The Beast', 'Sure Know Something', 'Hallowed Be Thy Name', 'Eruption', 'Where Eagles Dare', 'Welcome Home (Sanitarium)', 'Sweetest Thing', 'Surrender'],
    'Rating': [5, 4, 4, 4, 4, 4, 3, 3, 3, 3]
}

fig = px.bar(data, x='Song', y='Rating', title='Song Ratings')
print(fig.to_json())