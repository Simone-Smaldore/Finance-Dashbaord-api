from sqlalchemy.orm import Session
from datetime import datetime
from finance_dashboard_api.model.transazioni_uscite import TransazioniUscite


class DAOTransazioniService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TransazioniUscite).all()

    def get_by_id(self, transazione_id: int):
        return self.db.query(TransazioniUscite).filter_by(id=transazione_id).first()

    def create(
        self,
        descrizione: str,
        importo: float,
        id_utente: int,
        id_conto: int,
        tipologia_spesa: str = None,
        data_riferimento: datetime = None,
    ):
        nuova_transazione = TransazioniUscite(
            descrizione=descrizione,
            importo=importo,
            id_utente=id_utente,
            id_conto=id_conto,
            tipologia_spesa=tipologia_spesa,
            data_riferimento=data_riferimento,
        )
        self.db.add(nuova_transazione)
        self.db.commit()
        self.db.refresh(nuova_transazione)
        return nuova_transazione

    def update(self, transazione_id: int, **kwargs):
        transazione = self.get_by_id(transazione_id)
        if transazione:
            for key, value in kwargs.items():
                if hasattr(transazione, key) and value is not None:
                    setattr(transazione, key, value)
            self.db.commit()
            self.db.refresh(transazione)
        return transazione

    def delete(self, transazione_id: int):
        transazione = self.get_by_id(transazione_id)
        if transazione:
            self.db.delete(transazione)
            self.db.commit()
        return transazione
