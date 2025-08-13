from sqlalchemy.orm import Session

from finance_dashboard_api.model.utente import Utente


class DAOUtenteService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Utente).all()

    def get_by_id(self, utente_id: int):
        return self.db.query(Utente).filter_by(id=utente_id).first()

    def create(
        self, username: str, password: str, nome: str = None, cognome: str = None
    ):
        nuovo_utente = Utente(
            username=username, password=password, nome=nome, cognome=cognome
        )
        self.db.add(nuovo_utente)
        self.db.commit()
        self.db.refresh(nuovo_utente)
        return nuovo_utente

    def update(self, utente_id: int, **kwargs):
        utente = self.get_by_id(utente_id)
        if utente:
            for key, value in kwargs.items():
                if hasattr(utente, key) and value is not None:
                    setattr(utente, key, value)
            self.db.commit()
            self.db.refresh(utente)
        return utente

    def delete(self, utente_id: int):
        utente = self.get_by_id(utente_id)
        if utente:
            self.db.delete(utente)
            self.db.commit()
        return utente
