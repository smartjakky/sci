from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
meta = MetaData()
user = Table('user', meta,
             Column('id', Integer, primary_key=True),
             Column('name', String, nullable=False)
             )
postgre_config = {
    'user': 'postgres',
    'password': 'postgres',
    'host': '10.122.27.44',
    'schema': 'postgres'
}
db_uri = 'postgresql://{user}:{password}@{host}/{schema}'.format(**postgre_config)
db = create_engine(db_uri)


# MetaData.reflect():
print(user.metadata.tables)
user.metadata.reflect(bind=db)
print(user.metadata.tables)

# inspect()：检查已连接数据库表的信息
from sqlalchemy import inspect
inspector = inspect(bind=db)
print(inspector.get_table_names())
print(inspector.get_columns('ab_user'))
print(inspector.get_primary_keys('ab_user'))
