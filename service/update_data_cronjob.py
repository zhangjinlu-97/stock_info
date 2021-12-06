import time
import logging
import _thread as thread
from service import StockInfoService


def update_data_every_day(stock_info_service: StockInfoService):
    while True:
        print(time.asctime(time.localtime(time.time())), ': start update stock data')
        stock_info_service.update_stock_infos()
        print(time.asctime(time.localtime(time.time())), ': stock data updated')
        time.sleep(3600 * 24)  # 每天更新一次


def test_thread():
    while True:
        time.sleep(1)
        logging.warning('start update data')


if __name__ == '__main__':
    thread.start_new_thread(test_thread, ())
    print("---------")
    time.sleep(10)
