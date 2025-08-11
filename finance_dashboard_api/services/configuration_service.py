"""Contiene il servizio per la lettura dei dati di configurazione."""

import json
from pathlib import Path

from finance_dashboard_api.const import CONFIGURATION_FOLDER


class ConfigurationService:
    """Classe utilizzata per l'import della configurazione."""

    def __init__(self) -> None:
        """Inizializza la configurazione a partire dal file app-config."""
        config_file_url = Path(CONFIGURATION_FOLDER) / "app-config.json"
        with Path.open(config_file_url) as config_file:
            config = json.load(config_file)
        self.config = config

    def get_property(self, key: str) -> str:
        """Ottiene la proprietà con la chiave specificata."""
        return self.config[key]

    def get_int_property(self, key: str) -> int:
        """Ottiene la proprietà con la chiave specificata come intero."""
        return int(self.config[key])
