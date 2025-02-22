from sqlmodel import Session, select
from fastapi import HTTPException
from models import *

# -----------------------------------------------------------------------------

# Crear una nueva persona
def crear_persona(persona: Persona, session: Session):
    session.add(persona)
    session.commit()
    session.refresh(persona)
    return persona

# Obtener todas las personas
def obtener_personas(session: Session):
    query = select(Persona)
    personas = session.exec(query).all()
    return personas

# Obtener persona por ID
def obtener_persona_por_id(persona_id: int, session: Session):
    persona = session.get(Persona, persona_id)
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return persona

# Obtener personas por nombre
def obtener_personas_por_nombre(nombre: str, session: Session):
    statement = session.get(Persona).where(Persona.nombre == nombre)
    results = session.exec(statement)
    personas = results.all()
    if not personas:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return personas

# Actualizar una persona
def actualizar_persona(persona_id: int, persona_data: Persona, session: Session):
    persona = session.get(Persona, persona_id)
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    # Actualizar solo los campos modificados
    for field, value in persona_data.dict(exclude_unset=True).items():
        setattr(persona, field, value)

    session.commit()
    session.refresh(persona)
    return persona

# Eliminar una persona
def eliminar_persona(persona_id: int, session: Session):
    persona = session.get(Persona, persona_id)
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    session.delete(persona)
    session.commit()
    return {"message": "Persona eliminada correctamente"}

# -----------------------------------------------------------------------------

def crear_categoria(categoria: Categoria, session: Session):
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def obtener_categorias(session: Session):
    query = select(Categoria)
    categorias = session.exec(query).all()
    return categorias

def obtener_categoria_por_id(categoria_id: int, session: Session):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

def actualizar_categoria(categoria_id: int, categoria_data: Categoria, session: Session):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    # Actualizar solo los campos modificados
    for field, value in categoria_data.dict(exclude_unset=True).items():
        setattr(categoria, field, value)

    session.commit()
    session.refresh(categoria)
    return categoria

def eliminar_categoria(categoria_id: int, session: Session):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    session.delete(categoria)
    session.commit()
    return {"message": "Categoría eliminada correctamente"}
    
# -----------------------------------------------------------------------------

def crear_competencia(competencia: Competencia, session: Session):
    session.add(competencia)
    session.commit()
    session.refresh(competencia)
    return competencia

def obtener_competencias(session: Session):
    query = select(Competencia)
    competencias = session.exec(query).all()
    return competencias

def obtener_competencia_por_id(competencia_id: int, session: Session):
    competencia = session.get(Competencia, competencia_id)
    if not competencia:
        raise HTTPException(status_code=404, detail="Competencia no encontrada")
    return competencia

def actualizar_competencia(competencia_id: int, competencia_data: Competencia, session: Session):
    competencia = session.get(Competencia, competencia_id)
    if not competencia:
        raise HTTPException(status_code=404, detail="Competencia no encontrada")

    # Actualizar solo los campos modificados
    for field, value in competencia_data.dict(exclude_unset=True).items():
        setattr(competencia, field, value)

    session.commit()
    session.refresh(competencia)
    return competencia

def eliminar_competencia(competencia_id: int, session: Session):
    competencia = session.get(Competencia, competencia_id)
    if not competencia:
        raise HTTPException(status_code=404, detail="Competencia no encontrada")
    session.delete(competencia)
    session.commit()
    return {"message": "Competencia eliminada correctamente"}
    
# -----------------------------------------------------------------------------

def obtener_competencias_empleado(session: Session):
    query = select(CompetenciaEmpleado)
    competencias_empleado = session.exec(query).all()
    return competencias_empleado
    

def obtener_problemas(session: Session):
    query = select(Problema)
    problemas = session.exec(query).all()
    return problemas


def obtener_soluciones(session: Session):
    query = select(Solución)
    soluciones = session.exec(query).all()
    return soluciones


def obtener_autores(session: Session):
    query = select(Autor)
    autores = session.exec(query).all()
    return autores