import logging
from logging import log

from sqlalchemy import insert, select

from app_flask_archetype.repository.postgres.connection import PostgresConnection
from app_flask_archetype.repository.schema.computation import Computation

"""
    Guide:
        Place to implement your application's database related logic/concerns.
"""


class ComputationResultRepository:
    def __init__(self, database_connection: PostgresConnection) -> None:
        self.database_connection = database_connection
        self.source_schema = Computation(
            database_connection.get_connection_engine())

    def save(self, data) -> None:
        with self.database_connection.get_connection() as conn:
            result = conn.execute(
                insert(
                    self.source_schema.source_data_table()
                ),
                data,
            )
            conn.commit()

            log(logging.INFO, f"successfully saved {result.rowcount}")

    def retrieve(self):
        table_columns = (
            self.source_schema.source_data_table().c
        )
        with self.database_connection.get_connection() as conn:
            result = conn.execute(
                select(
                    table_columns.ParentLocation,
                    table_columns.ParentLocationCode,
                    table_columns.SpatialDim,
                    table_columns.TimeDim,
                    table_columns.NumericValue,
                )
            )
            return result.mappings().all()
