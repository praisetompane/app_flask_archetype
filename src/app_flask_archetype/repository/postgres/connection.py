from sqlalchemy import create_engine
from app_flask_archetype.repository.postgres.postgres_configuration import PostgresConfiguration
from sqlalchemy.engine import Engine, Connection


class PostgresConnection:
    def __init__(self, postgres_config: PostgresConfiguration) -> None:
        self.engine = create_engine(postgres_config.uri())

    def get_connection(self) -> Connection:
        return self.engine.connect()

    def get_connection_engine(self) -> Engine:
        return self.engine
