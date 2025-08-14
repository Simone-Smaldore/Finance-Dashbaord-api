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
from flask_jwt_extended import JWTManager
from injector import Binder

from finance_dashboard_api.const import CONFIGURATION_FOLDER
from finance_dashboard_api.api.routes import main_blueprint
from finance_dashboard_api.errors.error_register import register_errors
from finance_dashboard_api.logging_module.logger_initalizer import setup_logging
from finance_dashboard_api.services.api.api_transazioni_uscite_service import (
    APITransazioniUsciteService,
)
from finance_dashboard_api.services.configuration_service import ConfigurationService
from finance_dashboard_api.services.dao.dao_conto_service import DAOContoService
from finance_dashboard_api.services.dao.dao_transazioni_uscite_service import (
    DAOTransazioniService,
)
from finance_dashboard_api.services.dao.dao_utente_service import DAOUtenteService
from finance_dashboard_api.services.database_service import DatabaseService
from finance_dashboard_api.api.model.routes_transazioni_uscite import (
    api_transazioni_uscite_blueprint,
)
from finance_dashboard_api.api.model.routes_utente import (
    api_utente_blueprint,
)
from datetime import timedelta
import os

logger = logging.getLogger("finance_dashboard_backend")


def configure_injection(binder: Binder) -> None:
    """Configura l'injection.

    Questa funzione contiene le istruzioni per configurare l'injection.
    """
    binder.bind(ConfigurationService, to=ConfigurationService, scope=singleton)
    binder.bind(DatabaseService, to=DatabaseService, scope=singleton)
    binder.bind(DAOContoService, to=DAOContoService, scope=singleton)
    binder.bind(DAOTransazioniService, to=DAOTransazioniService, scope=singleton)
    binder.bind(DAOUtenteService, to=DAOUtenteService, scope=singleton)
    binder.bind(
        APITransazioniUsciteService, to=APITransazioniUsciteService, scope=singleton
    )


# Commentato setup loggin perchè non viene trovato correttamente il file. Se serve specificare path assoluto
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    origins=[os.getenv("FE_URL")],
)
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY_JWT")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(weeks=1)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_HTTPONLY"] = True
app.config["JWT_COOKIE_SECURE"] = True  # In produzione solo HTTPS!
app.config["JWT_COOKIE_SAMESITE"] = "None"  # Necessario per cross-site
app.register_blueprint(main_blueprint, url_prefix="")
app.register_blueprint(api_transazioni_uscite_blueprint, url_prefix="")
app.register_blueprint(api_utente_blueprint, url_prefix="")
jwt = JWTManager(app)
register_errors(app)
logger.debug("Starting application")
FlaskInjector(app=app, modules=[configure_injection])
