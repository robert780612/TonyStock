"""
Get the daily market index from the TWSE.

Copyright Robert 2016/02/25
"""

import re
import datetime
import time

from lxml import etree
import requests


class DownloadMarketIndex:
    """
    Query the market index of TW stock from http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php
    in the time range from start_day to end_day.
    Return the html source code of the page on the day.
    """

    def __init__(self, start_day, end_day):
        """
        :param start_day: class of datetime.date
        :param end_day: class of datetime.date
        :return: None
        """
        self.url = 'http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php'
        self.curr_day = start_day
        self.end_day = end_day

    def __iter__(self):
        return self

    def __next__(self):
        """
        Let self can use for looping by days.
        :return: Daily html source
        """
        if self.curr_day <= self.end_day:
            # Html post method,
            post_value = {'download': 'csv',
                          'qdate': '{0}/{1:0>2}/{2:0>2}'.format(self.curr_day.year - 1911,
                                                                self.curr_day.month,
                                                                self.curr_day.day),
                          'selectType': 'ALL'}
            res = requests.post(self.url, data=post_value)
            res.encoding = 'big5'
            self.curr_day += datetime.timedelta(1)
            return res.text
        else:
            raise StopIteration()


def csv_write(text, file_path):
    with open(file_path, 'w') as f:
        for x in text:
            f.write(x)


def dump_market_data(start_time, end_time):
    index_reader = DownloadMarketIndex(start_time, end_time)
    curr_time = start_time
    for x in index_reader:
        print('Download:' + curr_time.strftime('%Y/%m/%d'))
        csv_write(x, './data/raw/' + curr_time.strftime('%Y%m%d') + '.csv')
        time.sleep(10)
        curr_time = curr_time + datetime.timedelta(1)


# Deprecated
class ParseMarketIndex:
    """
    This class is deprecated. Because of TWSE supply csv download.
    There is arranged data in csv file in instead of parsing html.

    Parsing TW daily market stock page html source into 4 tables.
    Contains market_index, revenue_index, trade_index, updown_index
    """

    def __init__(self, html_src):
        """
        Constructor
        :param html_src: A string contains TWSE market index html source code.
        :return:
        """
        self.html = etree.HTML(html_src)
        self.tr = self.html.findall('.//tr')
        self.pas_string = []
        # Parsing table with delimiter '@,'
        for row in self.tr:
            s = ''
            for e in row:
                if len(e) > 0:
                    element = e.find('font')
                    s = s + element.text + '@,'
                else:
                    s = s + e.text + '@,'
            self.pas_string.append(s[:-2])
        prog = re.compile('^\d+年\d+月\d+日')
        self.date = prog.search(self.pas_string[0]).group(0)


if __name__ == "__main__":
    dump_market_data(datetime.datetime(2016, 1, 6), datetime.datetime(2016, 2, 29))
