from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DTOUtente:
    id: int
    created_at: datetime
    username: str
    nome: Optional[str]
    cognome: Optional[str]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "username": self.username,
            "nome": self.nome,
            "cognome": self.cognome,
        }
