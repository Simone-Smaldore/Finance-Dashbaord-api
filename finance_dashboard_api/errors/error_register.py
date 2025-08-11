"""File di per la registrazione degli errori nell'app flask."""

from typing import Literal

from flask import Flask, Response, jsonify
from werkzeug.exceptions import BadRequest, InternalServerError


def handle_bad_request(e: BadRequest) -> tuple[Response, Literal[400]]:
    """Funzione per la gestione dell'handling delle bad requests.

    Args:
        e (BadRequest): La richiesta arrivata in input.

    Returns:
        tuple[Response, Literal[400]]: Ritorna la risposta che verrà inviata in caso di BadRequest.
    """
    return (
        jsonify({"status": "error", "message": str(e.description)}),
        400,
    )


def handle_internal_server_error(
    e: InternalServerError,
) -> tuple[Response, Literal[500]]:
    """Funzione per la gestione dell'handling delle bad requests.

    Args:
        e (InternalServerError): La richiesta arrivata in input.

    Returns:
        tuple[Response, Literal[500]]: Ritorna la risposta che verrà inviata in caso di InternalServerError.
    """
    return (
        jsonify(
            {
                "status": "error",
                "message": f"Internal server error: {str(e.description)}",
            }
        ),
        500,
    )


def register_errors(app: Flask) -> None:
    """Funzione per la registrazione degli errori nell'app.

    Args:
        app (Flask): L'applicazione per cui registrare i gestori di errori.
    """
    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_error_handler(InternalServerError, handle_internal_server_error)
