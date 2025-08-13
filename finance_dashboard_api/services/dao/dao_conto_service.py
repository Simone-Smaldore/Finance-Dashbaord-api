from sqlalchemy.orm import Session

from finance_dashboard_api.model.conto import Conto


class DAOContoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Conto).all()

    def get_by_id(self, conto_id: int):
        return self.db.query(Conto).filter(Conto.id == conto_id).first()

    def create(self, descrizione: str):
        nuovo_conto = Conto(descrizione=descrizione)
        self.db.add(nuovo_conto)
        self.db.commit()
        self.db.refresh(nuovo_conto)
        return nuovo_conto

    def update(self, conto_id: int, descrizione: str):
        conto = self.get_by_id(conto_id)
        if conto:
            conto.descrizione = descrizione
            self.db.commit()
            self.db.refresh(conto)
        return conto

    def delete(self, conto_id: int):
        conto = self.get_by_id(conto_id)
        if conto:
            self.db.delete(conto)
            self.db.commit()
        return conto
