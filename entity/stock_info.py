import time

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
import json


class StockInfo(declarative_base()):
    __tablename__ = 'stock_info'
    id = Column('id', Integer, primary_key=True)
    symbol = Column('symbol', String(20))
    company_name = Column('company_name', String(255))
    refresh_time = Column('refresh_time', Integer)
    open = Column('open', Float)
    high = Column('high', Float)
    low = Column('low', Float)
    close = Column('close', Float)
    volume = Column('volume', Integer)

    def __init__(self, symbol, company_name, refresh_time, open, high, low, close, volume):
        self.symbol = symbol
        self.company_name = company_name
        self.refresh_time = refresh_time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    # 对象转换为json串
    def json(self):
        d = self.__dict__
        d.pop('_sa_instance_state')
        return json.dumps(d)


class StockInfoEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, StockInfo):
            d = obj.__dict__
            d.pop('_sa_instance_state')
            return d
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    si1 = StockInfo(symbol='AMD'
                    , company_name='Advanced Micro Devices Inc'
                    , refresh_time=time.mktime(time.strptime('2021-12-03 20:00:00', "%Y-%m-%d %H:%M:%S"))
                    , open=143.65
                    , high=143.6501
                    , low=143.5000
                    , close=143.5100
                    , volume=7715)
    si2 = StockInfo(symbol='AMD'
                    , company_name='Advanced Micro Devices Inc'
                    , refresh_time=time.mktime(time.strptime('2021-12-03 20:00:00', "%Y-%m-%d %H:%M:%S"))
                    , open=143.65
                    , high=143.6501
                    , low=143.5000
                    , close=143.5100
                    , volume=7715)
    sis = [si1, si2]
    print(json.dumps(sis, cls=StockInfoEncoder))
