"""Funzione principale dell'applicazione.

Contiene lo startup dell'applicazione.
"""

import logging
from pathlib import Path

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, singleton
from injector import Binder
from finance_dashboard_api.const import CONFIGURATION_FOLDER
from finance_dashboard_api.errors.error_register import register_errors
from finance_dashboard_api.logging_module.logger_initalizer import setup_logging
from finance_dashboard_api.controller.routes import main_blueprint
from finance_dashboard_api.services.configuration_service import ConfigurationService

from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger("finance_dashboard_api")


def main() -> None:
    """Esegue l'applicazione.

    Questa funzione contiene le istruzioni per eseguire l'applicazione.
    """
    setup_logging(Path(CONFIGURATION_FOLDER) / "config-logger.json")
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_blueprint, url_prefix="")
    register_errors(app)
    logger.debug("Starting application")
    FlaskInjector(app=app, modules=[configure_injection])
    app.run(host="127.0.0.1", port=8088)


def configure_injection(binder: Binder) -> None:
    """Configura l'injection.

    Questa funzione contiene le istruzioni per configurare l'injection.
    """
    binder.bind(ConfigurationService, to=ConfigurationService, scope=singleton)


if __name__ == "__main__":
    main()
