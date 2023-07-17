from pandas import DataFrame
import pandas.io.sql as psql

from db.engine import engine


def read_events() -> DataFrame:
    return psql.read_sql("SELECT * FROM events", engine)
