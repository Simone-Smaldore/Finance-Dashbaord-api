"""File di costanti."""

from pathlib import Path

PROJECT_FOLDER: str = str(
    f"{Path(Path(__file__).resolve()).parent}".replace("finance_dashboard_api", "")
)
CONFIGURATION_FOLDER: str = f"{PROJECT_FOLDER}/configurations"
