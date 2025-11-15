from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # название приложения
    app_name: str = "FastAPI Shop"
    # позволяет видеть ошибки
    debug: bool = False
    database_url: str = "sqlite:///./shop.db"
    # пути от которых принимаются бэкенд запросы
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"


settings = Settings()