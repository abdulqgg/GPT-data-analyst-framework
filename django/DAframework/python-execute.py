import json
import plotly.express as px

data = [
    ('The Trooper', 5),
    ('Untitled', 4),
    ('The Number Of The Beast', 4),
    ('Sure Know Something', 4),
    ('Hallowed Be Thy Name', 4),
    ('Eruption', 4),
    ('Where Eagles Dare', 3),
    ('Welcome Home (Sanitarium)', 3),
    ('Sweetest Thing', 3),
    ('Surrender', 3)
]

df = pd.DataFrame(data, columns=['Song', 'Rating'])

fig = px.bar(df, x='Song', y='Rating', title='Song Ratings')
print(fig.to_json())