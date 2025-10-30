from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///biblioteca_api.db"
engine = create_engine(DATABASE_URL, echo=True)
