from src.app_flask_archetype.repository.postgres.connection import PostgresConnection
from src.app_flask_archetype.repository.postgres.postgres_configuration import PostgresConfiguration
from src.app_flask_archetype.repository.computation_result_repository import ComputationResultRepository
import os

"""
    Guide:
        Place to initialize your application's common database objects.
"""

postgres_config = PostgresConfiguration(
    os.environ.get("POSTGRES_HOST"),
    os.environ.get("POSTGRES_PORT"),
    os.environ.get("POSTGRES_DB"),
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD")
)

postgres_connection = PostgresConnection(postgres_config)

computation_result_repository = ComputationResultRepository(
    postgres_connection)
