from sqlmodel import Session, select
from fastapi import HTTPException
from models import Persona

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

