import mysql.connector
from mysql.connector import Error

from .base_data_generator import BaseDataGenerator
from ..constants.sql_queries import SqlQueries


class MySqlDataGenerator(BaseDataGenerator):

    def generate_data(self, num_records, meta):
        connection = self.create_connection("localhost", 3306, "root", "root@123", "test")
        self.execute_query(connection, SqlQueries.CREATE_TABLE_QUERY.format(table_name=meta.get("table_name")))
        value_string = "('James', 25, 'male', 'USA'),"
        data = (value_string * num_records) + "('Elizabeth', 21, 'female', 'Canada');"
        self.execute_query(connection, SqlQueries.INSERT_QUERY.format(table_name=meta.get("table_name"), values=data))

    def create_connection(self, host_name, port, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                port=port,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
