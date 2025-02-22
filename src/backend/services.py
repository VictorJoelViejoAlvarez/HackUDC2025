from sqlmodel import Session, select
from fastapi import HTTPException
from models import Persona
from models import Categoria

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

