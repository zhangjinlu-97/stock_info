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


if __name__ == '__main__':
    si = StockInfo(symbol='AMD'
                   , company_name='Advanced Micro Devices Inc'
                   , refresh_time=time.mktime(time.strptime('2021-12-03 20:00:00', "%Y-%m-%d %H:%M:%S"))
                   , open=143.65
                   , high=143.6501
                   , low=143.5000
                   , close=143.5100
                   , volume=7715)
    update_stock_info(6, si)
