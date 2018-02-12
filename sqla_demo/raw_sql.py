from sqlalchemy import create_engine
import time
postgre_config = {
    'user': 'postgres',
    'password': 'postgres',
    'host': '10.122.27.44',
    'port': '5432',
    'schema': 'postgres'
}
db_uri = 'postgresql://{user}:{password}@{host}:{port}/{schema}'.format(**postgre_config)


# 原生sql访问数据库
db = create_engine(db_uri)
with db.connect() as con:
    res = con.execute('select count(*) from ab_user')
data = res.fetchone()
print(data)

from sqlalchemy.sql import text

with db.connect() as con:
    data = ({'name':'1','time':time.time.now()},
            {'name':'2','time':time.time.now()}
            )
    for line in data:
        res = con.execute(
            text("""
                insert into url(name, time) values (:name, :time)
                """, **line))
