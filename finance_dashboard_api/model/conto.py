from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, func
from finance_dashboard_api.services.database_service import DatabaseService

Base = DatabaseService().get_base()


class Conto(Base):
    __tablename__ = "conto"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    descrizione = Column(Text, nullable=False)
