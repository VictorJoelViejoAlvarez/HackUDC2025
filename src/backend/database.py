from sqlmodel import create_engine, Session
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Configuración desde .env
engine = create_engine(DATABASE_URL, echo=True)

# Obtener sesión de base de datos
def get_db():
    with Session(engine) as session:
        yield session