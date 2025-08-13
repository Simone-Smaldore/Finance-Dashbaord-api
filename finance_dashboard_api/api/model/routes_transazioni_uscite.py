import logging
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from injector import inject

from finance_dashboard_api.services.api.api_transazioni_uscite_service import (
    APITransazioniUsciteService,
)
from finance_dashboard_api.services.dao.dao_transazioni_uscite_service import (
    DAOTransazioniService,
)
from finance_dashboard_api.services.database_service import DatabaseService


api_transazioni_uscite_blueprint = Blueprint(
    "api_transazioni_uscite_blueprint", __name__
)
CORS(api_transazioni_uscite_blueprint)

logger = logging.getLogger(__name__)


db_service = DatabaseService()


@inject
@api_transazioni_uscite_blueprint.route("/transazioni_uscite", methods=["GET"])
@jwt_required()
def get_transazioni(
    db_service: DatabaseService,
    api_transazioni_uscite_service: APITransazioniUsciteService,
):
    session = db_service.get_session()
    dao_transazioni_service = DAOTransazioniService(session)
    result = api_transazioni_uscite_service.get_transazioni_uscite(
        dao_transazioni_service
    )
    return jsonify(result)


@inject
@api_transazioni_uscite_blueprint.route("/transazioni_uscite", methods=["POST"])
@jwt_required()
def create_transazione(
    db_service: DatabaseService,
    api_transazioni_uscite_service: APITransazioniUsciteService,
):
    session = db_service.get_session()
    dao_transazioni_service = DAOTransazioniService(session)
    data = request.get_json()
    result, code = api_transazioni_uscite_service.create_transaction(
        data, dao_transazioni_service
    )

    return (
        jsonify(result),
        code,
    )
