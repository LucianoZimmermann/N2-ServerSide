import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="n2"
        )
        if conn.is_connected():
            print("Conexão estabelecida com o banco de dados.")
        return conn
    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None

def create_all_tables(conn):
    if conn is not None:
        sql_table_ordered = (
            "CREATE TABLE IF NOT EXISTS ordered ("
            "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, "
            "descricao INT NOT NULL)"
        )

        sql_table_randomized = (
            "CREATE TABLE IF NOT EXISTS randomized ("
            "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, "
            "descricao INT NOT NULL)"
        )

        create_table(conn, sql_table_ordered)
        create_table(conn, sql_table_randomized)

        print("Tabelas criadas com sucesso.")

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(f"Ocorreu um erro ao criar a tabela: {e}")


def insert_values(conn, table_name, vector):
    if conn is not None:
        try:
            cursor = conn.cursor()

            insert_query = f"INSERT INTO {table_name} (descricao) VALUES (%s)"
            cursor.executemany(insert_query, [(value,) for value in vector])

            conn.commit()
            print(f"Valores inseridos com sucesso na tabela {table_name}.")

        except Error as e:
            print(f"Ocorreu um erro ao inserir valores na tabela {table_name}: {e}")

        finally:
            # Fechar o cursor
            cursor.close()
