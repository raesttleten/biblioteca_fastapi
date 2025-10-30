-----------Sistema de Gestión de Biblioteca------------

Descripción del proyecto:
El Sistema de Gestión de Biblioteca es una API desarrollada con FastAPI que permite administrar de forma eficiente los recursos de una biblioteca.
El sistema incluye operaciones CRUD (crear, leer, actualizar y eliminar) para gestionar información relacionada con libros, autores y usuarios.
Su propósito es facilitar la organización de los registros bibliográficos y permitir la integración con futuras interfaces gráficas o sistemas externos.

Tecnologías utilizadas:
Python 3.10+
FastAPI (framework principal para la creación de la API)
Uvicorn (servidor ASGI para ejecutar la aplicación)
Pydantic (validación de datos)
SQLAlchemy (ORM para la gestión de la base de datos)
SQLite (base de datos utilizada en el entorno de desarrollo)

Estructura del proyecto:
biblioteca_api/
│
├── main.py                 
├── models/                 
├── crud/                   
├── schemas/                
├── database.py             
└── README.md               

Clonar el repositorio:
git clone https://github.com/raesttleten/biblioteca_fastapi.git
cd biblioteca_fastapi

Instalar las dependencias necesarias:
pip install -r requirements.txt

Ejecutar la aplicación con Uvicorn:
uvicorn main:app --reload

Acceder a la documentación interactiva:
Documentación Swagger UI: http://127.0.0.1:8000/docs
Documentación ReDoc: http://127.0.0.1:8000/redoc

Sharick Hernández
Código: 67000979
Repository: https://github.com/raesttleten/biblioteca_fastapi.git

