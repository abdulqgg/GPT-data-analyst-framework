from dotenv import load_dotenv
import os
import openai
import subprocess
import sqlite3
import csv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are a sql expert in data analysis"},
        {"role": "user", "content": 
        '''Pretend you are a sql data analsyis,

            My database break down is as follows:

            customers:
            - Customerid
            - FirstName
            - LastName
            - Company
            - Address
            - City
            - State
            - Country
            - PostalCode
            - Phone
            - Fax
            - Email
            - SupportRepid

            employees:
            - Employeeid
            - LastName
            - FirstName
            - Title
            - ReportsTo
            - BirthDate
            - HireDate
            - Address

            invoices:
            - invoiceid
            - Customerid
            - InvoiceDate
            - BillingAddress
            - BillingCity

            invoice_items:
            - invoicelitemid
            - Invoiceid
            - Trackid
            - UnitPrice
            - Quantity

            albums:
            - Albumid
            - Title
            - Artistid

            tracks:
            - Trackid
            - Name
            - Albumid
            - MediaTypeid
            - Genreid
            - Composer
            - Milliseconds
            - Bytes
            - UnitPrice

            artists:
            - Artistid
            - Name

            playlist_track:
            - Playlistid
            - Trackid

            playlists:
            - Playlistid
            - Name

            media_types:
            - MediaTypeid
            - Name

            genres:
            - Genreid
            - Name


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

            Give me a list of all customer names with the count of unique invoices and the sum of unit price where the sum of unit price is greater than 45. Order by customer name
'''}
        ]
    )

query = chat_completion['choices'][0]['message']['content']

print(query)

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

cursor.execute(query)

rows = cursor.fetchall()

with open('extracted-data.csv', 'a', newline='') as f:
    f.write("\n")
    writer = csv.writer(f)
    writer.writerows(rows)

conn.close()