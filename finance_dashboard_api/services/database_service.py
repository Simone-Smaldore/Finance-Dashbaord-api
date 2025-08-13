import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


class DatabaseService:
    _instance = None  # riferimento alla singola istanza

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseService, cls).__new__(cls)
            cls._instance._init_engine()
        return cls._instance

    def _init_engine(self):
        self._db_host = os.environ.get("DB_Host")
        self._db_name = os.environ.get("DB_Database")
        self._db_user = os.environ.get("DB_Username")
        self._db_pass = os.environ.get("DB_Password")
        self._db_port = os.environ.get("DB_Port", "5432")

        self._engine = create_engine(self._build_url(), echo=False)
        self._SessionLocal = sessionmaker(bind=self._engine)
        self._Base = declarative_base()

    def _build_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self._db_user}:{self._db_pass}@{self._db_host}:{self._db_port}/{self._db_name}"
        )

    def get_engine(self):
        return self._engine

    def get_base(self):
        return self._Base

    def get_session(self) -> Session:
        return self._SessionLocal()
