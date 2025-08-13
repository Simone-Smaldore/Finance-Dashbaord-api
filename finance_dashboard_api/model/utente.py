from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, func

from finance_dashboard_api.services.database_service import DatabaseService


Base = DatabaseService().get_base()


class Utente(Base):
    __tablename__ = "utente"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    nome = Column(Text)
    cognome = Column(Text)
