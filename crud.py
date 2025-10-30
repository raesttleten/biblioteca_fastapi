from sqlmodel import Session, select
from fastapi import HTTPException, status
from models import Autor, Libro, LibroAutorLink

def crear_autor(session: Session, autor: Autor):
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor