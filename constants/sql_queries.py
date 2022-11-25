
class SqlQueries:

    CREATE_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT, 
        name TEXT NOT NULL, 
        age INT, 
        gender TEXT, 
        nationality TEXT, 
        PRIMARY KEY (id)
        ) ENGINE = InnoDB
    """
    

    INSERT_QUERY = "INSERT INTO {table_name} (name, age, gender, nationality) VALUES {values};"
