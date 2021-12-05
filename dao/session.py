from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://top18795876066:Zjl20151342019@rm-bp1k3z55sf0g51317bo.mysql.rds'
                       '.aliyuncs.com:3306/db_stock_info', pool_size=20, max_overflow=0)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
