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
    tipo_transazione: Optional[str]

    def to_dict(self):
        return {
            "id": self.id,
            "descrizione": self.descrizione,
            "importo": self.importo,
            "data_riferimento": (self.data_riferimento),
            "id_utente": self.id_utente,
            "id_conto": self.id_conto,
            "tipologia_spesa": self.tipologia_spesa,
            "tipo_transazione": self.tipo_transazione,
        }
