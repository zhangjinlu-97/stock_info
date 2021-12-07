import time
from service import StockInfoService


def update_data_every_day(stock_info_service: StockInfoService):
    while True:
        print(time.asctime(time.localtime(time.time())), ': start update stock data')
        stock_info_service.update_stock_infos()
        print(time.asctime(time.localtime(time.time())), ': stock data updated')
        time.sleep(3600 * 24)  # 每天更新一次
