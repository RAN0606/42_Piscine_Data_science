import psycopg2

def excute_sql():
    dbname = "piscineds"
    user = "rliu"
    password = "mysecretpassword"
    host = "localhost"
    port = "5432"

    try: 
        with open("fix_items_table.sql", "r") as sql_file:
            sql_script1 = sql_file.read()
        with open("fusion.sql", "r") as sql_file:
            sql_script2 = sql_file.read()
        print("SQL code has been imported!")
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connected to postgres!")
        cursor = conn.cursor()
        cursor.execute(sql_script1)
        print("SQL script fix_items_table executed successfully!")
        print("Data has been fetched from the table.")
        cursor.execute(sql_script2)
        print("SQL script fusion executed successfully!")
        print("Data has been fetched from the table.")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    excute_sql()
