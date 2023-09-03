# GPT Data Analyst Framework

Welcome to my data analysis project! Inspired by a research paper I read, I've developed a framework that leverages the power of natural language processing (NLP) for data analysis. The core feature of this project is its ability to convert natural language queries into SQL statements, execute these statements to extract relevant data, and create visualizations for a more intuitive understanding of the results.

## Website

https://abdulqg.pythonanywhere.com/index/

## Main Features

1. **Natural Language Data Analysis**: This project is designed to accept natural language queries. With the help of the GPT-3.5-Turbo API, these queries are transformed into executable SQL statements.

2. **Data Extraction**: The SQL queries are executed on a connected database, with results extracted and stored in a CSV file (`extracted-data.csv`).

3. **Data Visualization**: The framework also offers the capability to visualize the extracted data using Python (plotly), providing a clear, comprehensible depiction of the results.

## Technologies

The following technologies and languages have been used in this project:

1. **Python**: The primary language for scripting and development.

2. **SQLite**: Essential for data extraction and manipulation.

3. **GPT API**: Used for the conversion of natural language queries into SQL statements.

4. **Django**: Web framework for Python.

5. **PythonAnywhere**: Hosting service.

## Results

The main deliverable of this project is the `extracted-data.csv` file, containing data extracted through SQL queries. Additionally, if visualizations are opted for, a set of Python-generated visuals will be produced.

## How to Use

Youtube tutorial https://youtu.be/12gOkmMs8qg

To use this project, kindly follow these steps:

1. Set up your environment variables. Save your `OPENAI_API_KEY` in .env 
2. Connect to your SQL database. I've used `chinook.db`, a sample database, in this project.
3. Enter your database table and column names into `database-info.txt` in same format as example
4. Run `gpt-sql.py` to initiate the data extraction process. This script will convert your natural language input into SQL queries, execute them on the connected database, and save the results as a CSV called `extracted-data.csv`.
5. If you wish to visualize the data, run `gpt-python.py`. This script will create visualizations using the data extracted in the previous step.

Please note that you may need to install specific Python libraries if they aren't already present in your environment.

### Libraries and Installation

**Standard Libraries**:
- `os`, `subprocess`, `sqlite3`, `csv`: Included with Python.

**Third-Party Libraries**:
- `dotenv`: Environment variables management.
- `openai`: OpenAI API access.
- `pandas`: Data analysis.

Install the third-party libraries using:

`
pip install python-dotenv openai pandas
`

Ensure you have the required libraries before running the project.

## Credits

This project draws inspiration from a research paper I read. I have carried out the implementation and development of this idea into a functioning project. https://arxiv.org/abs/2305.15038

## Screenshots

![Screenshot 2023-08-11 at 23 20 00](https://github.com/abdulqgg/GPT-data-analyst-framework/assets/43912641/b5fc0985-856e-422c-833f-95af90804eea)



