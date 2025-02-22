import psycopg2
import psycopg2.errorcodes
import psycopg2.extras
import sys

# Conectarse a la BD:
def connect_db():
    try:
        conn = psycopg2.connect("")
        conn.autocommit = False
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        sys.exit(1)

# Desconectarse de la BD:
def disconnect_db(conn):
    conn.commit()
    conn.close()


