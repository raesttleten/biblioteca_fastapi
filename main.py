from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import engine, crear_db
from models import Autor, Libro
from crud import crear_autor, crear_libro, eliminar_autor
from schemas import AutorCreate, LibroCreate

app = FastAPI(title="Sistema de Gestión de Biblioteca")

def get_session():
    with Session(engine) as session:
        yield session

crear_db()

@app.post("/autores")
def nuevo_autor(autor: AutorCreate, session: Session = Depends(get_session)):
    return crear_autor(session, Autor.from_orm(autor))

@app.get("/autores")
def listar_autores(pais: str | None = None, session: Session = Depends(get_session)):
    query = select(Autor)
    if pais:
        query = query.where(Autor.pais_origen == pais)
    return session.exec(query).all()

@app.post("/libros")
def nuevo_libro(libro: LibroCreate, session: Session = Depends(get_session)):
    libro_model = Libro(titulo=libro.titulo, isbn=libro.isbn, anio_publicacion=libro.anio_publicacion, copias_disponibles=libro.copias_disponibles)
    return crear_libro(session, libro_model, libro.autores_ids)

@app.get("/libros")
def listar_libros(anio: int | None = None, session: Session = Depends(get_session)):
    query = select(Libro)
    if anio:
        query = query.where(Libro.anio_publicacion == anio)
    return session.exec(query).all()

@app.delete("/autores/{autor_id}")
def borrar_autor(autor_id: int, session: Session = Depends(get_session)):
    return eliminar_autor(session, autor_id)