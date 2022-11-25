from ..constants.source_types import SourceTypes
from .my_sql_data_generator import MySqlDataGenerator
from .postgres_data_generator import PostgresDataGenerator

class DataGeneratorFactory():

    DATA_GENERATOR_MAP = {
        SourceTypes.MY_SQL: MySqlDataGenerator,
        SourceTypes.POSTGRES: PostgresDataGenerator
    }

    def get_data_generator_class(self, source_type):
        return self.DATA_GENERATOR_MAP.get(source_type)
