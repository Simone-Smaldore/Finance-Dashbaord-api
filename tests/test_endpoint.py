"""File di test contente i test degli endpoint."""

from collections.abc import Generator
from typing import Any

import pytest
from flask.testing import FlaskClient
from finance_dashboard_api.app_gunicorn import app


@pytest.fixture
def client() -> Generator[FlaskClient, Any, None]:
    with app.test_client() as client:
        yield client


def test_health_check(client: FlaskClient) -> None:
    response = client.get("/healthCheck")
    codice_200 = 200
    assert response.status_code == codice_200
    assert response.json == {"status": "Server up"}
