import time
import requests
from dao import StockInfoDao
from entity import StockInfo

STOCK_BASE_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=5min&apikey={' \
                 'apikey}&symbol={symbol}'
COMPANY_BASE_URL = 'https://www.alphavantage.co/query?function=OVERVIEW&apikey={apikey}&symbol={symbol}'
API_KEYS = 'FBI8NKWZZ810Q454'


def stock_url(apikey, symbol) -> str:
    return STOCK_BASE_URL.format(apikey=apikey, symbol=symbol)


def company_url(apikey, symbol) -> str:
    return COMPANY_BASE_URL.format(apikey=apikey, symbol=symbol)


def get_new_stock_info(stock_symbol: str) -> StockInfo:
    """
    获取最新股票信息
    :param stock_symbol: 需要获取的股票Symbol
    :return StockInfo
    """
    # 获取股价信息
    surl = stock_url(API_KEYS, stock_symbol)
    stock_info = requests.get(surl)
    stock_dict = stock_info.json()
    # 获取公司信息
    curl = company_url(API_KEYS, stock_symbol)
    company_info = requests.get(curl)
    company_dict = company_info.json()
    # 将json数据转换为StockInfo对象，并返回
    last_time = stock_dict['Meta Data']['3. Last Refreshed']
    new_record = stock_dict['Time Series (5min)'][last_time]
    return StockInfo(symbol=stock_symbol
                     , company_name=company_dict['Name']
                     , refresh_time=time.mktime(time.strptime(last_time, "%Y-%m-%d %H:%M:%S"))
                     , open=float(new_record['1. open'])
                     , high=float(new_record['2. high'])
                     , low=float(new_record['3. low'])
                     , close=float(new_record['4. close'])
                     , volume=int(new_record['5. volume'])
                     )


class StockInfoService(object):

    def __init__(self):
        self.stock_info_dao = StockInfoDao()

    def get_stock_infos(self):
        """
        获取股票信息
        :return: 股票信息列表 StockInfo[]
        """
        return self.stock_info_dao.get_stock_infos()

    def add_new_stock_info(self, symbol: str):
        """
        新增股票信息
        :param symbol:
        """
        stock_info = get_new_stock_info(symbol)
        self.stock_info_dao.insert_stock_info(stock_info)

    def update_stock_infos(self):
        """
        获取最新股票信息
        这里由于免费API的频率限制，采用每30s更新一次的策略
        """
        stock_infos = self.stock_info_dao.get_stock_infos()
        for si in stock_infos:
            time.sleep(30)  # 每30s更新一个数据
            new_si = get_new_stock_info(si.symbol)
            self.stock_info_dao.update_stock_info(si.id, new_si)

    def delete_stock_info(self, symbol):
        """
        删除指定股票信息
        :param symbol: 要删除股票的symbol
        """
        self.stock_info_dao.delete_stock_info(symbol)


if __name__ == '__main__':
    url = stock_url(API_KEYS, 'IBM')
    print(url)
    stock_data = requests.get(url).json()
    print(type(stock_data))
    print(stock_data)
