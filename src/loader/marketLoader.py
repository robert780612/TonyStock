"""
Let the data of market parser load into the database.

Copyright Robert 2016/02/27
"""

import sqlite3 as sql
import datetime

from src.reader import marketReader as mr


class TonyDBLoader:
    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sql.connect(self.db_path)
        self.c = self.conn.cursor()
        return self

    def _re_create_table(self):
        """
        Only run when first build database.
        This function build all tables in the database.
        :return: None
        """
        # SQLite time datatype YYYY-MM-DD HH:MM:SS.SSS
        self.c.execute('''CREATE TABLE trading_day
                       (trading integer, date text)''')
        self.c.execute('''CREATE TABLE market_index
                       (symbol text, indexed real, type text, difference real, percent real, date text,
                       PRIMARY KEY (symbol, date)
                       )''')

    def __loading_daily_data(self, date):
        """

        :param day: datetime.datetime
        :return:
        """
        print('Load:' + date.strftime('%Y/%m/%d'))
        data = mr.DailyReader(date.year, date.month, date.day)
        if not data.trading_day:
            return 'Not a trading day'
        format_date = date.strftime('%Y-%m-%d')
        # Insert a row of data
        for x in data.market:
            self.c.execute("INSERT INTO market_index "
                           "VALUES ('{}','{}','{}','{}','{}','{}')".format(x[0], x[1], x[2], x[3], x[4], format_date))

        # Save (commit) the changes
        self.conn.commit()
        return 0

    def loading_data(self, start_day, end_day):
        curr_day = start_day
        while curr_day <= end_day:
            self.__loading_daily_data(curr_day)
            curr_day += datetime.timedelta(1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)
        self.conn.close()

# with sqlite3.connect('tony.db') as conn:
#     c = conn.cursor()
#     c.execute('select * from market_stocks')
#     print(c.fetchall())

if __name__ == "__main__":
    with TonyDBLoader('./tony_db.sqlite3') as a:
        # a._re_create_table()
        a.loading_data(datetime.datetime(2016, 1, 1), datetime.datetime(2016, 2, 29))