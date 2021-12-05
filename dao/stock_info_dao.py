import time

from dao.session import DBSession
from entity import StockInfo


def get_stock_infos():
    """
    查询所有股票信息
    :return: 股票信息列表StockInfo[]
    """
    # 创建连接
    conn = DBSession()
    # 查询stock_info
    stock_info = conn.query(StockInfo).all()
    # 关闭数据库连接
    conn.close()
    return stock_info


def insert_stock_info(stock_info: StockInfo):
    """
    新增股票信息
    :param stock_info: 股票信息
    """
    conn = DBSession()
    conn.add(stock_info)
    conn.commit()
    conn.close()


def update_stock_info(sid: int, new_stock_info: StockInfo):
    """
    更新股票信息
    :param sid:
    :param new_stock_info:
    """
    conn = DBSession()
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


def delete_stock_info(symbol: str):
    """
        删除指定股票信息
        :param symbol: 要删除股票的symbol
    """
    conn = DBSession()
    conn.query(StockInfo).filter(StockInfo.symbol == symbol).delete()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    si = StockInfo(symbol='NTES'
                   , company_name='NetEase Inc'
                   , refresh_time=time.mktime(time.strptime('2021-12-03 16:55:00', "%Y-%m-%d %H:%M:%S"))
                   , open=101.9900
                   , high=101.9900
                   , low=101.9900
                   , close=101.9900
                   , volume=100)
    insert_stock_info(si)
