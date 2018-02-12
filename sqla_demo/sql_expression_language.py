from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import pymysql

pymysql.install_as_MySQLdb()
mysql_config = {
    'user': 'root',
    'password': '123',
    'host': 'localhost',
    'port': '3306',
    'schema': 'ihome'
}
db_uri = 'mysql://{user}:{password}@{host}:{port}/{schema}'.format(**mysql_config)
db = create_engine(db_uri)
meta = MetaData(db)
areas = Table('ih_area_info', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String(32), nullable=False),
              Column('create_time', DateTime),
              Column('update_time', DateTime)
              )
# select()
select_obj = select([areas.c.name])
with db.connect() as con:
    rs = con.execute(select_obj)
# insert()
areas.insert().values(id=12, name='name')
# Select.limit()
select_obj = select_obj([areas.c.name]).limit(2)
# Select.where()
select_obj = select_obj([areas.c.id]).where(areas.c.id > 1)
# and_()
from sqlalchemy.sql import and_
select_obj = select_obj([areas.c.id]).where(and_(areas.c.id > 1, areas.c.id < 10))
# Column.like()
select_obj = select_obj([areas.c.id]).where(areas.c.name.like('%name'))
