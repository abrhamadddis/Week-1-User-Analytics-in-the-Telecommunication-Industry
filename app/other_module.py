from sqlalchemy import create_engine
import pandas as pd
"""
a function that connect to the local database
"""
def create_conn():
    engine = None
    try:
        # Create an engine that connects to PostgreSQL server
        engine = create_engine('postgresql://postgres:telecom@localhost:5432/telecom')
        print("Connection successful")
    except Exception as error:
        print(error)

    return engine

"""
a function that that accept engine, and table_name as an argument and return pandas data fream
"""
def fetch_data(engine, table_name):
    df = None
    try:
        # Execute a query and fetch all the rows into a DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", engine)
    except Exception as error:
        print(error)

    return df
