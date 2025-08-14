import logging
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (
    create_access_token,
    get_csrf_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from injector import inject

from finance_dashboard_api.services.api.api_utenti_service import APIUtentiService
from finance_dashboard_api.services.dao.dao_utente_service import DAOUtenteService
from finance_dashboard_api.services.database_service import DatabaseService
import os


api_utente_blueprint = Blueprint("api_utente_blueprint", __name__)
CORS(
    api_utente_blueprint,
    supports_credentials=True,
    origins=[os.getenv("FE_URL")],
)

logger = logging.getLogger(__name__)
db_service = DatabaseService()


@api_utente_blueprint.route("/me", methods=["GET"])
@jwt_required()
def me():
    current_user_id = get_jwt_identity()
    current_username = get_jwt().get("username")
    return jsonify({"id": current_user_id, "username": current_username})


@inject
@api_utente_blueprint.route("/login", methods=["POST"])
def login(api_utenti_service: APIUtentiService):
    session = db_service.get_session()
    dao_utente_service = DAOUtenteService(session)
    data = request.get_json()
    message, access_token, code = (
        api_utenti_service.get_utente_by_username_and_password(
            data=data, dao_utente_service=dao_utente_service
        )
    )
    response = jsonify(message)
    if access_token is not None:
        set_access_cookies(response, access_token)
        response.set_cookie("csrf_access_token", get_csrf_token(access_token))
    return response, code


@jwt_required()
@api_utente_blueprint.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200
