from dotenv import dotenv_values
from src.app_flask_quickstart.repository.postgres.connection import PostgresConnection
from src.app_flask_quickstart.repository.postgres.postgres_configuration import PostgresConfiguration
from src.app_flask_quickstart.repository.computation_result_repository import ComputationResultRepostory

"""
    Guide:
        Place to initilize your application's common database objects.
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

computation_result_repository = ComputationResultRepostory(postgres_connection)
