from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('', pool_size=20, max_overflow=0)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
