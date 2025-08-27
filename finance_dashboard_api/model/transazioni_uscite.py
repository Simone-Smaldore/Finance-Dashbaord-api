from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, Float, ForeignKey, func

from finance_dashboard_api.services.database_service import DatabaseService


Base = DatabaseService().get_base()


class TransazioniUscite(Base):
    __tablename__ = "transazioni_uscite"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    descrizione = Column(Text)
    data_riferimento = Column(TIMESTAMP(timezone=False))
    importo = Column(Float, nullable=False)
    id_utente = Column(BigInteger, ForeignKey("utente.id"), nullable=False)
    id_conto = Column(BigInteger, ForeignKey("conto.id"), nullable=False)
    tipologia_spesa = Column(Text)
    tipo_transazione = Column(Text)
