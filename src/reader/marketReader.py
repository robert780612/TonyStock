"""
Read the daily market index csv file.
Return the specific format.

Copyright Robert 2016/02/28
"""


ZERO_EXPRESSOR = ['--', '---']

class DailyReader:
    """

    """
    def __init__(self, y, m, d):
        """

        :param y: AD year
        :param m: month
        :param d: day
        :return:
        """
        # Read the csv file
        with open('./data/raw/{0}{1:>02}{2:>02}.csv'.format(y, m, d)) as f:
            self.all_table = f.readlines()
        self.date = '{0}{1:>02}{2:>02}.csv'.format(y, m, d)

        # Whether that day is a trading day or not.
        if len(self.all_table)<20:
            self.trading_day = False
            return
        else:
            self.trading_day = True

        for i, x in enumerate(self.all_table):
            x = x.replace('"','').strip()
            eles = x.split(',')
            if eles[0] == '指數':
                # print(eles)
                break

        # Table : Market
        # Column: Name | Index | Direction | Change | Change(%)
        # Type  : text | num   | text      | num    | num
        start = i + 1
        self.market = []
        for i, x in enumerate(self.all_table[start:]):
            x = x.replace('"', '').strip()
            eles = x.split(',')

            # Specific condition handling
            if eles[0] == '報酬指數':
                # print(eles)
                break
            if eles[1] in ZERO_EXPRESSOR:
                continue
            if eles[3] in ZERO_EXPRESSOR:
                eles[3] = 0
            if eles[4] in ZERO_EXPRESSOR:
                eles[4] = 0

            eles[1] = float(eles[1])
            eles[3] = float(eles[3])
            eles[4] = float(eles[4])
            self.market.append(eles)

        # Table : Return
        # Column: Name | Index | Direction | Change | Change(%)
        # Type  : text | num   | text      | num    | num
        start = start + i + 1
        self.ret = []
        for i, x in enumerate(self.all_table[start:]):
            x = x.replace('"', '').strip()
            eles = x.split(',')

            # Specific condition handling
            if eles[0] == '成交統計':
                # print(eles)
                break
            if eles[1] in ZERO_EXPRESSOR:
                continue
            if eles[3] in ZERO_EXPRESSOR:
                eles[3] = 0
            if eles[4] in ZERO_EXPRESSOR:
                eles[4] = 0
            eles[1] = float(eles[1])
            eles[3] = float(eles[3])
            eles[4] = float(eles[4])
            self.ret.append(eles)

        # TODO the other table

if __name__ == "__main__":
    a = DailyReader(2016, 1, 4)
    print(a.market)
    print(len(a.market))
    print(a.ret)