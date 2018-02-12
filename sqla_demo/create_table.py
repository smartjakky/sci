from sqlalchemy import create_engine, MetaData, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship
from sqlalchemy import table, column, select

# ===============数据库配置================
DB_URI = 'hana://lidm1:lidm1(SCI)@10.122.13.22:30353'
DB_SCHEMA = 'PLATFORM'
# ===============数据库配置================

# ===============初始化连接================
db = create_engine(DB_URI)
metadata = MetaData(bind=db, schema=DB_SCHEMA)
Model = declarative_base(bind=db, metadata=metadata)
session = sessionmaker(bind=db)()
# ===============初始化连接================

# ===============要添加的表模型================
# class EmbedReport(Model):
#     """嵌入报表"""
#
#     __tablename__ = 'embed_report'
#
#     id = Column(Integer, Sequence(__tablename__ + '_id_seq'), primary_key=True)
#     report_name = Column(String(50), unique=True, nullable=False)  # 报表名称
#     target_sys = Column(String(20), nullable=False)  # 系统名称
#     report_path = Column(String(100))  # 报表路径
#     report_query = Column(Text)  # 请求参数：json类型


class Demo(Model):

    __tablename__ = 'demo'

    id = Column(Integer, Sequence(__tablename__ + '_id_seq'), primary_key=True)


# ===============要添加的表模型================
session.add(Demo)
session.commit()