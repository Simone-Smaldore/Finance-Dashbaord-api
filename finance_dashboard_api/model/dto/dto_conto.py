from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DTOConto:
    id: int
    created_at: datetime
    descrizione: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "descrizione": self.descrizione,
        }
