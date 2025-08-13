from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DTOTransazioniUscite:
    id: int
    descrizione: Optional[str]
    importo: float
    data_riferimento: Optional[datetime]
    id_utente: int
    id_conto: int
    tipologia_spesa: Optional[str]

    def to_dict(self):
        return {
            "id": self.id,
            "descrizione": self.descrizione,
            "importo": self.importo,
            "data_riferimento": (
                self.data_riferimento.isoformat() if self.data_riferimento else None
            ),
            "id_utente": self.id_utente,
            "id_conto": self.id_conto,
            "tipologia_spesa": self.tipologia_spesa,
        }
