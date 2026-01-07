instructions = [
    "DROP TABLE IF EXISTS todo;",
    "DROP TABLE IF EXISTS \"user\";",
    """
        CREATE TABLE \"user\" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        );
    """,
    """
        CREATE TABLE todo (
            id SERIAL PRIMARY KEY,
            created_by INT NOT NULL,
            user_id INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE,
            FOREIGN KEY (created_by) REFERENCES \"user\"(id)
        );
    """,
]
