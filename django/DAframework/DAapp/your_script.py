from dotenv import load_dotenv
import os
import openai
import subprocess
import sqlite3
import csv
from django.http import FileResponse

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











'''
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

cursor.execute(query)

rows = cursor.fetchall()

with open('extracted-data.csv', 'w', newline='') as f:
    #f.write("\n")
    writer = csv.writer(f)
    writer.writerows(rows)

conn.close()
'''