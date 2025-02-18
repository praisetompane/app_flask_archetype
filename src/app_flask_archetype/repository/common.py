from dotenv import dotenv_values
from src.app_flask_archetype.repository.postgres.connection import PostgresConnection
from src.app_flask_archetype.repository.postgres.postgres_configuration import PostgresConfiguration
from src.app_flask_archetype.repository.computation_result_repository import ComputationResultRepository

"""
    Guide:
        Place to initialize your application's common database objects.
"""

config = dotenv_values(".env")

postgres_config = PostgresConfiguration(
    config["POSTGRES_HOST"],
    config["POSTGRES_PORT"],
    config["POSTGRES_DB"],
    config["POSTGRES_USER"],
    config["POSTGRES_PASSWORD"],
)

postgres_connection = PostgresConnection(postgres_config)

computation_result_repository = ComputationResultRepository(
    postgres_connection)
