from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

engine = create_engine(
    # получаем database url который указан в настройках
    settings.database_url,
    # нельзя делать несколько запросов ондовременно
    connect_args={"check_same_thread": False}
)
# создает сессии на соединение базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# описание таблиц / бд
Base = declarative_base()

def get_db():
     # вызывает новую сессию когда нужна база данных
    db = SessionLocal()
    try:
        # ищет нужную информацию
        yield db
    finally:
        #в конце закрывает сессию
        db.close()

def init_db():
    # иницилизирует базу данных с помощью engine
    Base.metadata.create_all(bind=engine)