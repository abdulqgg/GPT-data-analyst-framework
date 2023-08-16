import os
import openai
import subprocess
import sqlite3
import csv
from django.http import FileResponse
import pandas as pd

def your_function(txt_file_path, db_file_path, api_key, user_query):
    with open(txt_file_path, 'r') as file:
        database_info = file.read()

    openai.api_key = api_key

    user_query = user_query

    chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are a sql expert in data analysis"},
        {"role": "user", "content": 
        f'''Pretend you are a sql data analsyis,

            My database break down is as follows:

            {database_info}
            I want you to give only the sql code as a output so for example:

            Input: How do i select all the customers first names
            Output: 
            SELECT FirstName FROM customers;

            input: Update a albums name to "new name" where its id is 101
            Output:
            UPDATE albums
            SET Title = 'new name'
            WHERE Albumid = 101;

            -----


            {user_query}
            
        '''}
        ])

    query = chat_completion['choices'][0]['message']['content']

    # Connect to the SQLite database and execute the query
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    # Write the results to a CSV file
    with open('extracted-data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # Create a FileResponse to send the CSV file to the client
    response = FileResponse(open('extracted-data.csv', 'rb'))
    response['Content-Disposition'] = 'attachment; filename="extracted-data.csv"'

    return response

def python_visualise():
    df = pd.read_csv('extracted-data.csv')

    data_string = df.to_string()

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a python expert in data analysis"},
            {"role": "user", "content": 
            f'''Pretend you are a python data analsyis,

                I want you ot give only the python code as a output so for example:

                Example 1:
                Input: How to print something
                Output: print("hello world")

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

                Visualise this data using plotly: {data_string}

    '''}
            ]
        )

    execute = chat_completion['choices'][0]['message']['content']

    with open('python-execute.txt', 'w') as f:
        f.write(execute)

    subprocess.run(["python", 'python-execute.txt'])