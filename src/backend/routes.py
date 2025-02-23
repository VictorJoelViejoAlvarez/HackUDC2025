from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_db
from models import Persona
from services import *

router = APIRouter()

@router.post("/personas/", response_model=Persona)
def crear(persona: Persona, session: Session = Depends(get_db)):
    return crear_persona(persona, session)

@router.get("/personas/", response_model=list[Persona])
def listar(session: Session = Depends(get_db)):
    return obtener_personas(session)

@router.get("/personas/nombres/{persona_nombre}", response_model=list[Persona])
def obtener_por_nombre(nombre: str, session: Session = Depends(get_db)):
    return obtener_personas_por_nombre(nombre, session)

@router.get("/personas/ids/{persona_id}", response_model=Persona)
def obtener(persona_id: int, session: Session = Depends(get_db)):
    return obtener_persona_por_id(persona_id, session)

@router.put("/personas/{persona_id}", response_model=Persona)
def actualizar(persona_id: int, persona_data: Persona, session: Session = Depends(get_db)):
    return actualizar_persona(persona_id, persona_data, session)

@router.delete("/personas/{persona_id}")
def eliminar(persona_id: int, session: Session = Depends(get_db)):
    return eliminar_persona(persona_id, session)

#----------------------------------------------------------------------------------------------

@router.post("/categorias/", response_model=Categoria)
def crear(categoria: Categoria, session: Session = Depends(get_db)):
    return crear_categoria(categoria, session)

@router.get("/categorias/{categoria_id}", response_model=Categoria)
def obtener(categoria_id: int, session: Session = Depends(get_db)):
    return obtener_categoria_por_id(categoria_id, session)

@router.get("/categorias/", response_model= list[Categoria])
def obtener(session: Session = Depends(get_db)):
    return obtener_categorias(session)

@router.get("/competencias/", response_model= list[Competencia])
def obtener(session: Session = Depends(get_db)):
    return obtener_competencias(session)

@router.get("/CompetenciaEmpleado/", response_model=list[CompetenciaEmpleado])
def obtener_competencias_de_empleado(session: Session = Depends(get_db)):
    return obtener_competencias_empleado(session)

@router.get("/problemas/", response_model= list[Problema])
def obtener(session: Session = Depends(get_db)):
    return obtener_problemas(session)

@router.get("/solucion/", response_model= list[Solucion])
def obtener(session: Session = Depends(get_db)):
    return obtener_soluciones(session)

@router.get("/autor/", response_model= list[Autor])
def obtener(session: Session = Depends(get_db)):
    return obtener_autores(session)

