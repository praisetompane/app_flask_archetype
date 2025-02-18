from sqlalchemy import MetaData, Table

"""
    Guide:
        Place to implement your application's database schema configuration in line with migrations created.
"""


class Computation:
    def __init__(self, engine) -> None:
        self.engine = engine
        self.table_store = MetaData(schema="computation")
        self.table_store.reflect(bind=self.engine)

    def source_data_table(self) -> Table:
        return self.table_store.tables["computation.computation_result"]
