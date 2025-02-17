from src.app_flask_quickstart.etl.malaria_annual_confirmed_cases_etl import (
    MalariaAnnualConfirmedCasesETL,
)

from src.app_flask_quickstart.repository.malaria_annual_confirmed_cases_repository import (
    MalariaAnnualConfirmedCasesRepository,
)
from src.app_flask_quickstart.repository.common import postgres_connection


malaria_annual_confirmed_cases_etl = MalariaAnnualConfirmedCasesETL(
    MalariaAnnualConfirmedCasesRepository(postgres_connection))

"""
    Registry of supported ETLs.
"""
etls = {
    "Malaria Annual Confirmed Cases": malaria_annual_confirmed_cases_etl,
}
