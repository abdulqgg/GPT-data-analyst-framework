# Project Notes

## File Descriptions

### gpt-python.py
This file is used to visualize `extracted-data.csv`. It leverages GPT to generate Python code, which is saved to `python-execute.txt`, and then executes that code in a Python environment.

### gpt-sql.py
This file is used to generate `extracted-data.csv`. It takes the user's query about the data, generates SQL code, executes the query on the dataset, and produces the extracted data.

## Workflow Overview

1. **Data Extraction**:
   - Use `gpt-sql.py` to handle user queries about the dataset.
   - The script generates appropriate SQL code.
   - The SQL code is executed to query the dataset and produce `extracted-data.csv`.

2. **Data Visualization**:
   - Use `gpt-python.py` to visualize the data from `extracted-data.csv`.
   - The script generates Python code to create the visualizations.
   - The generated code is saved to `python-execute.txt`.
   - The code is then executed in a Python environment to produce the visualizations.
