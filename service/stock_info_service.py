import json
import time
import requests
from dao import stock_info_dao
from entity import StockInfo

stock_base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=5min&apikey=4MXQG2ZWFM6GK8R2' \
                 '&symbol='
company_base_url = 'https://www.alphavantage.co/query?function=OVERVIEW&apikey=4MXQG2ZWFM6GK8R2&symbol='


def get_stock_infos():
    """
    获取股票信息
    :return: 股票信息列表 StockInfo[]
    """
    return stock_info_dao.get_stock_infos()


def add_new_stock_info(symbol: str):
    """
    新增股票信息
    :param symbol:
    """
    stock_info = get_new_stock_info(symbol)
    stock_info_dao.insert_stock_info(stock_info)


def update_stock_infos():
    """
    获取最新股票信息
    """
    stock_infos = stock_info_dao.get_stock_infos()
    for si in stock_infos:
        new_si = get_new_stock_info(si.symbol)
        stock_info_dao.update_stock_info(si.id, new_si)


def get_new_stock_info(stock_symbol: str) -> StockInfo:
    """
    获取最新股票信息
    :param stock_symbol: 需要获取的股票Symbol
    :return 返回StockInfo列表
    """
    # mock
    if stock_symbol == 'INTC':
        return StockInfo(symbol=stock_symbol
                         , company_name="Intel Corporation"
                         , refresh_time=time.mktime(time.strptime("2021-12-03 20:00:00", "%Y-%m-%d %H:%M:%S"))
                         , open=49.25
                         , high=49.25
                         , low=49.25
                         , close=49.25
                         , volume=254
                         )
    # 获取股价信息
    stock_info = requests.get(stock_base_url + stock_symbol)
    stock_data = stock_info.json()
    # 获取公司信息
    company_info = requests.get(company_base_url + stock_symbol)
    company_data = company_info.json()
    # 将json数据转换为StockInfo对象，并返回
    # 解析股价信息json数据为dict
    stock_dict = json.loads(stock_data)
    last_time = stock_dict['Meta Data']['3. Last Refreshed']
    new_record = stock_dict['Time Series (5min)'][last_time]
    # 解析公司信息json数据为dict
    company_dict = json.loads(company_data)
    company_name = company_dict['Name']
    return StockInfo(symbol=stock_symbol
                     , company_name=company_name
                     , refresh_time=time.mktime(time.strptime(last_time, "%Y-%m-%d %H:%M:%S"))
                     , open=float(new_record['1. open'])
                     , high=float(new_record['2. high'])
                     , low=float(new_record['3. low'])
                     , close=float(new_record['4. close'])
                     , volume=int(new_record['5. volume'])
                     )
