from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class TransazioneUscitaValidator(BaseModel):
    descrizione: str = Field(..., min_length=1)
    data_riferimento: datetime
    importo: float = Field(..., gt=0)
    id_utente: int = Field(..., gt=0)
    id_conto: int = Field(..., gt=0)
    tipologia_spesa: str = Field(..., min_length=1)
    tipo_transazione: str = Field(..., min_length=1)

    @field_validator("descrizione", "tipologia_spesa", mode="before")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if v is None or str(v).strip() == "":
            raise ValueError("Il campo non può essere nullo o vuoto")
        return v

    @field_validator("tipo_transazione", mode="before")
    @classmethod
    def valid_tipo_transazione(cls, v: str) -> str:
        allowed = {"Entrata", "Uscita"}
        if v not in allowed:
            raise ValueError(f"tipo_transazione deve essere uno tra {allowed}")
        return v
