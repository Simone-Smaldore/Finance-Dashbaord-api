"""Funzione principale dell'applicazione per gunicorn.

Contiene lo startup dell'applicazione da utilizzare con gunicorn in docker.
Il contenuto è parallelo rispetto ad app.py. Serve un file a parte per
permettere a gunicorn di trovare l'attributo app nel file.
Questo file viene inoltre utilizzato anche nei test che necessitano di trovare
l'app come per gunicorn.
"""

import logging
from pathlib import Path

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, singleton
from injector import Binder

from finance_dashboard_api.const import CONFIGURATION_FOLDER
from finance_dashboard_api.controller.routes import main_blueprint
from finance_dashboard_api.errors.error_register import register_errors
from finance_dashboard_api.logging_module.logger_initalizer import setup_logging
from finance_dashboard_api.services.configuration_service import ConfigurationService

import os

print(os.getenv("DB_Host"))


logger = logging.getLogger("lhub_backend")


def configure_injection(binder: Binder) -> None:
    """Configura l'injection.

    Questa funzione contiene le istruzioni per configurare l'injection.
    """
    binder.bind(ConfigurationService, to=ConfigurationService, scope=singleton)


# Commentato setup loggin perchè non viene trovato correttamente il file. Se serve specificare path assoluto
app = Flask(__name__)
CORS(app)
app.register_blueprint(main_blueprint, url_prefix="")
register_errors(app)
logger.debug("Starting application")
FlaskInjector(app=app, modules=[configure_injection])
