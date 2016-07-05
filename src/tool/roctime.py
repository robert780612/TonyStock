"""
This script gives a convenience tool for transformation from Common Era to ROC Era.
Example: 2016/02/25 -> 105/02/25

Copyright Robert 2016/02/26
"""

from datetime import *


class ROCDateTime:
    """
    Only support one format output like 105/01/01
    """
    def __init__(self, rocy, m, d):
        self.year = rocy + 1911
        self.month = m
        self.day = d
        self.__date = datetime(self.year, self.month, self.day)

    def __str__(self):
        return str(self.year-1911)+'/'+str(self.month)+'/'+str(self.day)

    def __add__(self, other):
        if not isinstance(other, timedelta):
            return NotImplemented
        rr = self.__date + other
        return ROCDateTime(rr.year-1911, rr.month, rr.day)

    def __eq__(self, other):
        if not (isinstance(other, ROCDateTime) or isinstance(other, datetime)):
            return NotImplemented
        else:
            return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)


if __name__ == "__main__":
    a = ROCDateTime(104, 12, 31)
    b = datetime(2015, 10, 31)
    c = ROCDateTime(104, 12, 31)
    print(a)
    print(b)
    print(a+timedelta(1))
    print(a == b)
    print(a == c)