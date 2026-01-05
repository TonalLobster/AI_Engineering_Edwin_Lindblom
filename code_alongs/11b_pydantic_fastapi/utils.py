from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"
DATA_PATH.mkdir(exist_ok=True)

def query_duckdb(sql_code, parameters=None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        if parameters:
            cursor = conn.execute(sql_code, parameters)
        else:
            cursor = conn.execute(sql_code)

        sql_lower = sql_code.strip().casefold()
        if sql_lower.startswith(("select", "from", "desc", "pragma")):
            return cursor.df()
