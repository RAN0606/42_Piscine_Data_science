import psycopg2

def excute_sql():
    dbname = "piscineds"
    user = "rliu"
    password = "mysecretpassword"
    host = "localhost"
    port = "5432"

    try:
        with open("remove_duplicates.sql", "r") as sql_file:
            sql_script = sql_file.read()
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
        cursor.execute(sql_script)
        print("SQL script executed successfully!")
        print("Data has been fetched from the table.")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    excute_sql()
