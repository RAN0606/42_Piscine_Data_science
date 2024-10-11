import os
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table

def table_exists(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        print(f"Table {table_name} already exist")
    return table_name in metadata.tables


def load(path, tableName,engine):
    try:
        if not table_exists(engine, tableName):
            print(f"Table {tableName} doesn't exist, creating...")
            data = pd.read_csv(path)
            data_types = {
                "event_time": sqlalchemy.DateTime(),
                "event_type": sqlalchemy.types.String(length=255),
                "product_id": sqlalchemy.types.Integer(),
                "price": sqlalchemy.types.Float(),
                "user_id": sqlalchemy.types.BigInteger(),
                "user_session": sqlalchemy.types.UUID(as_uuid=True)  # Corrected the data type
            }
            data.to_sql(tableName, engine, index=False, dtype=data_types)
            print(f"Table {tableName} created")

    except Exception as error:
        print(f"An error occurred: {error}")

def automatic_create_all(folder_path):
    try:
        engine = create_engine("postgresql://rliu:mysecretpassword@localhost:5432/piscineds")
        for file in os.listdir(folder_path):
            if file.endswith('.csv'):
                filepath = os.path.join(folder_path, file)
                load(filepath,os.path.splitext(file)[0], engine)
        engine.dispose()
    except Exception as error:
        print(f"An error occurred: {error}")
        
if __name__ == "__main__":
    automatic_create_all("../customer")