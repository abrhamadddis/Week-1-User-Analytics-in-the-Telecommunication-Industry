from sqlalchemy import create_engine
import pandas as pd

def create_conn():
    engine = None
    try:
        # Create an engine that connects to PostgreSQL server
        engine = create_engine('postgresql://postgres:telecom@localhost:5432/telecom')
        print("Connection successful")
    except Exception as error:
        print(error)

    return engine

def fetch_data(engine):
    df = None
    try:
        # Execute a query and fetch all the rows into a DataFrame
        df = pd.read_sql_query("SELECT * FROM xdr_data  ;", engine)
    except Exception as error:
        print(error)

    return df