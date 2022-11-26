
class SqlQueries:

    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS {table_name} {create_table_columns_query}"

    INSERT_QUERY = "INSERT INTO {table_name} {insert_record_column_names} VALUES {values};"
