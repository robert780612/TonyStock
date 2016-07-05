
import datetime

from src.parser.marketParser import dump_market_data
from src.loader.marketLoader import TonyDBLoader

start_day = datetime.datetime(2016, 3, 1)
end_day = datetime.datetime(2016, 3, 14)
dump_market_data(start_day, end_day)
with TonyDBLoader('./tony_db.sqlite3') as a:
        a.loading_data(start_day, end_day)