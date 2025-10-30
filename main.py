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