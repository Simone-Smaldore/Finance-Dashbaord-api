from flask_jwt_extended import get_jwt_identity
from finance_dashboard_api.model.dto.dto_transazioni_uscite import DTOTransazioniUscite
from finance_dashboard_api.services.dao.dao_transazioni_uscite_service import (
    DAOTransazioniService,
)
from datetime import datetime
from typing import Union, Tuple


class APITransazioniUsciteService:

    def get_transazioni_uscite(
        self,
        dao_transazioni_service: DAOTransazioniService,
    ) -> list[DTOTransazioniUscite]:
        transazioni = dao_transazioni_service.get_by_utente_id(
            utente_id=get_jwt_identity()
        )
        return [
            DTOTransazioniUscite(
                id=t.id,
                descrizione=t.descrizione,
                importo=t.importo,
                data_riferimento=t.data_riferimento,
                id_utente=t.id_utente,
                id_conto=t.id_conto,
                tipologia_spesa=t.tipologia_spesa,
            )
            for t in transazioni
        ]

    def create_transaction(
        self,
        data: dict,
        dao_transazioni_service: DAOTransazioniService,
    ) -> Tuple[Union[DTOTransazioniUscite, dict], int]:
        # Controllo dei campi richiesti
        if not all(k in data for k in ("id_conto", "transazione")):
            return {"error": "Missing required fields"}, 400

        id_utente = get_jwt_identity()
        id_conto = data["id_conto"]
        t_data = data["transazione"]

        required_trans_fields = [
            "descrizione",
            "importo",
            "tipologia_spesa",
            "data_riferimento",
        ]
        if not all(f in t_data for f in required_trans_fields):
            return {"error": "Missing fields in transazione"}, 400

        # Convertiamo la data da string ISO8601 a datetime
        data_riferimento = datetime.fromisoformat(t_data["data_riferimento"])

        # Creiamo la transazione
        transazione = dao_transazioni_service.create(
            descrizione=t_data["descrizione"],
            importo=t_data["importo"],
            id_utente=id_utente,
            id_conto=id_conto,
            tipologia_spesa=t_data["tipologia_spesa"],
            data_riferimento=data_riferimento,
        )

        return (
            DTOTransazioniUscite(
                id=transazione.id,
                descrizione=transazione.descrizione,
                importo=transazione.importo,
                data_riferimento=transazione.data_riferimento,
                id_utente=transazione.id_utente,
                id_conto=transazione.id_conto,
                tipologia_spesa=transazione.tipologia_spesa,
            ),
            201,
        )

    def delete_transaction(
        self,
        transazione_id: int,
        dao_transazioni_service: DAOTransazioniService,
    ) -> tuple[dict, int]:
        transazione = dao_transazioni_service.get_by_id(transazione_id)

        if not transazione:
            return {"error": "Transazione non trovata"}, 404
        if transazione.id_utente != int(get_jwt_identity()):
            return {"error": "Non autorizzato"}, 403
        dao_transazioni_service.delete(transazione_id)
        return {"message": "Transazione eliminata con successo"}, 200
