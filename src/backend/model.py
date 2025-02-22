import psycopg2
import psycopg2.errorcodes
import psycopg2.extras
import sys

# Error genérico:
def gerror(e):
    print(f"Error genérico:\nCódigo: {e.pgcode}\nMensaje: {e.pgerror}")

# Persona ---------------------------------------------------------------------

def insertPersona(connection, nombre, apellido1, apellido2, empleado, telefono, email):
    with connection.cursor() as cur:
        try:
            cur.execute(
                "insert into persona (nombre, apellido1, apellido2, empleado, telefono, email) values (%s, %s, %s, %s, %s, %s);",
                (nombre, apellido1, apellido2, empleado, telefono, email)
            )
            connection.commit() # Confirmar cambios
            return True
        except psycopg2.Error as e:
            if e.pgcode == psycopg2.errorcodes.UNDEFINED_TABLE:
                print("Error: La tabla persona no existe.")
            elif e.pgcode == psycopg2.errorcodes.INVALID_TEXT_REPRESENTATION:
                print("Error: Los valores introducidos no son válidos.")
                gerror(e)
            else:
                gerror(e)
            connection.rollback() # Deshacer cambios si hay error