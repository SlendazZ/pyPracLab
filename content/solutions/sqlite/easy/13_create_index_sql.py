def index_sql(table: str, column: str) -> str:
    return f'CREATE INDEX IF NOT EXISTS idx_{table}_{column} ON {table}({column})'
