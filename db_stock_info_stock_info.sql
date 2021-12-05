create table stock_info
(
    id           int auto_increment
        primary key,
    symbol       varchar(20)  default '' not null comment '股票代号',
    company_name varchar(255) default '' not null comment '股票名称',
    open         double                  null comment '开盘价',
    high         double                  null comment '最高价',
    low          double                  null comment '最低价',
    close        double                  null comment '收盘价',
    volume       double                  null comment '股票发行量',
    refresh_time bigint                  null comment '最近刷新时间戳',
    constraint stock_info_id_symbol_date_uindex
        unique (id, symbol)
);

INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (1, 'IBM', 'International Business Machines Corporation', 119.11, 119.11, 119.11, 119.11, 307, 1638531600);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (2, 'TSLA', 'Tesla Inc', 1008.21, 1008.25, 1007, 1008, 7388, 1638532800);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (3, 'AAPL', 'Apple Inc', 161.38, 161.43, 161.2, 161.25, 21095, 1638532800);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (4, 'GOOG', 'Alphabet Inc', 2848.26, 2848.26, 2848.26, 2848.26, 218, 1638531000);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (5, 'MSFT', 'Microsoft Corporation', 322.7, 322.85, 322.7, 322.7, 3062, 1638532800);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (6, 'AMD', 'Advanced Micro Devices Inc', 143.65, 143.6501, 143.5, 143.51, 7715, 1638532800);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (13, 'QCOM', 'QUALCOMM Incorporated', 176.4999, 176.4999, 176.4999, 176.4999, 500, 1638532800);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (20, 'NTES', 'NetEase Inc', 101.99, 101.99, 101.99, 101.99, 100, 1638521700);
INSERT INTO db_stock_info.stock_info (id, symbol, company_name, open, high, low, close, volume, refresh_time) VALUES (23, 'INTC', 'Intel Corporation', 49.25, 49.25, 49.25, 49.25, 254, 1638532800);
