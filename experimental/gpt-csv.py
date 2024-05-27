from dotenv import load_dotenv
import os
from openai import OpenAI
import subprocess
import pandas as pd

df = pd.read_csv('Delivery truck trip data.csv')

columns = df.dtypes

load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

user_query = input("Please enter your query: ")

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are a python expert in data analysis"},
        {"role": "user", "content": 
        f'''Pretend you are a python data analsyis,

            I want you to give only the python code with all libaries imported as a output with no speech marks so for example:

            Example 1:
            Input: How to print something
            Output: 
            print("hello world")

            Example 2:
            Input: How to create a bar chart
            Output:
            import matplotlib.pyplot as plt
            categories = ['A', 'B', 'C']
            values = [10, 15, 7]
            plt.bar(categories, values)
            plt.show()

            Example 3:
            Input: how to craete a scatter plot in pyton
            Output:
            import matplotlib.pyplot as plt
            x_values = [1, 2, 3, 4, 5]
            y_values = [5, 7, 6, 8, 7]
            plt.scatter(x_values, y_values)
            plt.xlabel('X Values')
            plt.ylabel('Y Values')
            plt.title('Scatter Plot')
            plt.show()

            Example 4:
            Input: Create me a bar chart example using plotpy
            Output:
            import plotly.graph_objects as go
            fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
            quantities = [10, 15, 7, 10, 5]
            fig = go.Figure([go.Bar(x=fruits, y=quantities)])
            fig.update_layout(title_text='Fruit Quantities', xaxis_title='Fruit', yaxis_title='Quantity')
            fig.show()



            -----

            Using these columns for my dataframe : f{columns},
            
            Give me the python code to f{user_query} and for my df using this:
             
              df = pd.read_csv('Delivery truck trip data.csv') '''}])

execute = chat_completion.choices[0].message.content

if execute.startswith('`'):
    execute = execute[3:-5]

if execute.startswith("python"):
    execute = execute[7:]

with open('python-execute-csv.txt', 'w') as f:
    f.write(execute)

result = subprocess.run(["python", 'python-execute-csv.txt'], capture_output=True, text=True)

print("Standard Output:", result.stdout)

print(result)