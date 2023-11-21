import json
import plotly.graph_objects as go

# Define the data
songs = ['The Trooper', 'Untitled', 'The Number Of The Beast', 'Sure Know Something',
         'Hallowed Be Thy Name', 'Eruption', 'Where Eagles Dare', 'Welcome Home (Sanitarium)',
         'Sweetest Thing', 'Surrender']
ratings = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3]

# Create the bar chart
fig = go.Figure(data=go.Bar(x=songs, y=ratings))

# Set the layout
fig.update_layout(title='Songs Ratings',
                  xaxis_title='Songs',
                  yaxis_title='Ratings')

# Show the chart
print(fig.to_json())