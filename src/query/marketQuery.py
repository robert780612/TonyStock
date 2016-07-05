"""
Query the market index data from db.

Copyright Robert 2016/03/05
"""

import sqlite3 as sql

from TonyStock.settings import DATABASES


class DBQuery:
    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sql.connect(self.db_path)
        self.c = self.conn.cursor()
        return self

    def query(self, query_str):
        self.c.execute(query_str)
        return self.c.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)
        self.conn.close()


if __name__ == "__main__":
    db_path = DATABASES['default']['NAME']
    with DBQuery(db_path) as a:
        data = a.query('select distinct symbol from market_index')
    for x in data:
        print(x[0])
