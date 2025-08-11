"""Contiene le routes principali dell'applicazione."""

import logging
from flask import Blueprint, Response, jsonify
from flask_cors import CORS

main_blueprint = Blueprint("main_blueprint", __name__)
CORS(main_blueprint)

logger = logging.getLogger(__name__)


@main_blueprint.route("/healthCheck", methods=["GET"])
def health_check() -> Response:
    """Route per la verifica del funzionamento delle API.

    Args:
        configuration_service (ConfigurationService): Il servizio per ottenere le
        proprietà di configurazione viene iniettato tramite dependency injection.

    Returns:
        Response: Risponde con 200 se il server è in piedi.
    """
    logger.info("Health check endpoint called")
    return jsonify({"status": "Server up"}), 200
