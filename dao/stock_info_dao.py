import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity import StockInfo

DB_URL = 'mysql+mysqlconnector://username:password@xxxxx:3306' \
         '/db_stock_info'


class StockInfoDao(object):
    def __init__(self):
        # 初始化数据库连接:
        self.engine = create_engine(DB_URL, pool_size=20, max_overflow=0)
        # 创建DBSession类型:
        self.db_session = sessionmaker(bind=self.engine)

    def get_stock_infos(self):
        """
        查询所有股票信息
        :return: 股票信息列表StockInfo[]
        """
        # 创建连接
        conn = self.db_session()
        # 查询stock_info
        stock_info = conn.query(StockInfo).all()
        # 关闭数据库连接
        conn.close()
        return stock_info

    def insert_stock_info(self, stock_info: StockInfo):
        """
        新增股票信息
        :param stock_info: 股票信息
        """
        conn = self.db_session()
        conn.add(stock_info)
        conn.commit()
        conn.close()

    def update_stock_info(self, sid: int, new_stock_info: StockInfo):
        """
        更新股票信息
        :param sid:
        :param new_stock_info:
        """
        conn = self.db_session()
        stock_info = conn.query(StockInfo).filter(StockInfo.id == sid).first()
        stock_info.company_name = new_stock_info.company_name
        stock_info.refresh_time = new_stock_info.refresh_time
        stock_info.open = new_stock_info.open
        stock_info.high = new_stock_info.high
        stock_info.low = new_stock_info.low
        stock_info.close = new_stock_info.close
        stock_info.volume = new_stock_info.volume
        conn.commit()
        conn.close()

    def delete_stock_info(self, symbol: str):
        """
            删除指定股票信息
            :param symbol: 要删除股票的symbol
        """
        conn = self.db_session()
        conn.query(StockInfo).filter(StockInfo.symbol == symbol).delete()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    dao = StockInfoDao()
    si = StockInfo(symbol='NTES'
                   , company_name='NetEase Inc'
                   , refresh_time=time.mktime(time.strptime('2021-12-03 16:55:00', "%Y-%m-%d %H:%M:%S"))
                   , open=101.9900
                   , high=101.9900
                   , low=101.9900
                   , close=101.9900
                   , volume=100)
    dao.insert_stock_info(si)
