import json

from flask import Flask
from service import stock_info_service
from entity.stock_info import StockInfoEncoder

app = Flask(__name__)


@app.route('/get/stock/info')
def get_stock_info():  # put application's code here
    stock_info_list = stock_info_service.get_stock_infos()
    return json.dumps(stock_info_list, cls=StockInfoEncoder)


@app.route('/update/stock/info')
def update_stock_info():
    """
    从yahoo finance更新最新股票信息
    """
    stock_info_service.update_stock_infos()
    return ''


@app.route("/add/new/stock/<symbol>")
def add_new_stock(symbol):
    """
    新增股票信息
    """
    stock_info_service.add_new_stock_info(symbol)
    return ''


@app.route("/delete/stock/<symbol>")
def delete_stock_info(symbol):
    """
    删除指定股票信息
    :param symbol: 要删除股票的symbol
    """
    stock_info_service.delete_stock_info(symbol)
    return ''


if __name__ == '__main__':
    app.run()
