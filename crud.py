from sqlmodel import Session, select
from fastapi import HTTPException, status
from models import Autor, Libro, LibroAutorLink

def crear_autor(session: Session, autor: Autor):
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

def crear_libro(session: Session, libro: Libro, autores_ids: list[int]):
    # Regla 1: ISBN único
    if session.exec(select(Libro).where(Libro.isbn == libro.isbn)).first():
        raise HTTPException(status_code=409, detail="ISBN duplicado")
    session.add(libro)
    session.commit()
    for id_autor in autores_ids:
        session.add(LibroAutorLink(autor_id=id_autor, libro_id=libro.id))
    session.commit()
    session.refresh(libro)
    return libro

def eliminar_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    # Regla 3: cascada
    libros = session.exec(select(Libro).join(LibroAutorLink).where(LibroAutorLink.autor_id == autor_id)).all()
    for libro in libros:
        session.delete(libro)
    session.delete(autor)
    session.commit()