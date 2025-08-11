"""Raccolta di funzioni di utilità per il logging.

È presente una funzione per effettuare il setup del logging.
"""

import json
import logging.config
from pathlib import Path


def setup_logging(file_path: Path) -> None:
    """Setup the application logger passing the file path of a json setup file.

    Args :
        file_path (str): the relative file path to the logger json file
    """
    with Path.open(file_path) as file_conf:
        logging_config = json.load(file_conf)
    logging.config.dictConfig(config=logging_config)
