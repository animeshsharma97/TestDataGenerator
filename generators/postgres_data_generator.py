import psycopg2

from .base_data_generator import BaseDataGenerator
from ..constants.source_types import SourceTypes
from ..constants.sql_queries import SqlQueries
from ..utils.fake_data_generator import FakeDataGenerator
from ..utils.sql_utils import SqlUtils


class PostgresDataGenerator(BaseDataGenerator):

    def setup(self, meta):
        self.column_type_list, self.insert_record_column_names, self.create_table_columns_query = SqlUtils.get_sql_queries_metadata(SourceTypes.POSTGRES, meta)
        connection = None
        try:
            connection = self.create_connection("localhost", 5430, "postgres", "postgres", "test")
            self.execute_query(connection, SqlQueries.CREATE_TABLE_QUERY.format(table_name=meta.get("table_name"), create_table_columns_query=self.create_table_columns_query))
        finally:
            connection.close()

    def generate_data(self, num_records, meta):
        data = FakeDataGenerator().generate_fake_data(num_records, self.column_type_list)
        num_records_string = ", ".join(["%s"] * num_records)
        connection = None
        try:
            connection = self.create_connection("localhost", 5430, "postgres", "postgres", "test")
            self.execute_query(connection, SqlQueries.INSERT_QUERY.format(table_name=meta.get("table_name"), insert_record_column_names=self.insert_record_column_names, values=num_records_string), data)
        finally:
            connection.close()

    def cleanup(self):
        pass

    def create_connection(self, host_name, port, user_name, user_password, db_name):
        connection = None
        connection = psycopg2.connect(
            host=host_name,
            user=user_name,
            port=port,
            password=user_password,
            database=db_name,
            connect_timeout=600
        )
        print("Connection to Postgres successful")
        return connection

    def execute_query(self, connection, query, values=None):
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
