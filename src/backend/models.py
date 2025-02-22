from sqlmodel import SQLModel, Field

class Persona(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    apellido1: str
    apellido2: str
    empleado: bool
    telefono: str
    email: str
