from ..constants.source_types import SourceTypes


class SqlUtils:

    @staticmethod
    def get_sql_queries_metadata(source_type, meta):
        columns_meta = meta.get("columns_meta")
        primary_key = meta.get("primary_key", None)
        column_type_list = [column_meta.get("type") for column_meta in columns_meta if SqlUtils.include_column_in_query(source_type, column_meta)]
        create_table_columns_query = "("
        insert_record_column_names = "("
        for column_meta in columns_meta:
            if source_type == SourceTypes.POSTGRES and "SERIAL" in column_meta.get("options"):
                create_table_columns_query += f"{column_meta.get('name')} {column_meta.get('options', '')},"
            else:
                create_table_columns_query += f"{column_meta.get('name')} {column_meta.get('type')} {column_meta.get('options', '')},"
            if SqlUtils.include_column_in_query(source_type, column_meta):
                insert_record_column_names += f"{column_meta.get('name')},"
        if source_type == SourceTypes.MY_SQL and primary_key:
            create_table_columns_query += f"PRIMARY KEY ({primary_key})"
        else:
            create_table_columns_query = create_table_columns_query[:-1]
        
        insert_record_column_names = insert_record_column_names[:-1]
        insert_record_column_names += ")"
        create_table_columns_query += ")"
        return column_type_list, insert_record_column_names, create_table_columns_query

    @staticmethod
    def include_column_in_query(source_type, column_meta):
        return (source_type == SourceTypes.MY_SQL and column_meta.get("options") != "AUTO_INCREMENT") or (source_type == SourceTypes.POSTGRES and "SERIAL" not in column_meta.get("options"))
