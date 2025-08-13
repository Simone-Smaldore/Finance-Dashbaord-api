from flask_jwt_extended import create_access_token
from typing import Tuple
from finance_dashboard_api.model.dto.dto_utente import DTOUtente
from finance_dashboard_api.services.dao.dao_utente_service import DAOUtenteService


class APIUtentiService:

    def get_utente_by_username_and_password(
        self,
        data: dict,
        dao_utente_service: DAOUtenteService,
    ) -> Tuple[dict, str, int]:
        username = data.get("username")
        password = data.get("password")

        utente = dao_utente_service.get_by_username_and_password(
            username=username, password=password
        )
        if utente is None:
            return {"error": "Credenziali errate"}, None, 401
        access_token = create_access_token(
            identity=str(utente.id), additional_claims={"username": utente.username}
        )
        response = {"message": "Login successful"}
        return response, access_token, 200
