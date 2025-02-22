from sqlmodel import SQLModel, Field

class Persona(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    apellido1: str
    apellido2: str
    empleado: bool
    telefono: str
    email: str

class Categoria(SQLModel, table=True):
    id: int = Field(primary_key=True)
    categoria: str

class Competencia(SQLModel, table=True):
    id: int = Field(primary_key=True)
    competencia: str
    categoria_id: int

class CompetenciaEmpleado(SQLModel, table=True):
    empleado_id: int = Field(primary_key=True)
    competencia_id: int = Field(primary_key=True)
    obtencion: str
    verificado: bool

class Problema(SQLModel, table=true):
    id: int = Field(primary_key=True)
    problema: str
    descripcion: str
    competencia_id: int

class Solucion(SQLModel, table=true):
    id: int = Field(primary)