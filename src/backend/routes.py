from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_db
from models import Persona
from services import (
    crear_persona,
    obtener_personas,
    obtener_persona_por_id,
    actualizar_persona,
    eliminar_persona
)

router = APIRouter()

@router.post("/personas/", response_model=Persona)
def crear(persona: Persona, session: Session = Depends(get_db)):
    return crear_persona(persona, session)

@router.get("/personas/", response_model=list[Persona])
def listar(session: Session = Depends(get_db)):
    return obtener_personas(session)

@router.get("/personas/{persona_id}", response_model=Persona)
def obtener(persona_id: int, session: Session = Depends(get_db)):
    return obtener_persona_por_id(persona_id, session)

@router.put("/personas/{persona_id}", response_model=Persona)
def actualizar(persona_id: int, persona_data: Persona, session: Session = Depends(get_db)):
    return actualizar_persona(persona_id, persona_data, session)

@router.delete("/personas/{persona_id}")
def eliminar(persona_id: int, session: Session = Depends(get_db)):
    return eliminar_persona(persona_id, session)