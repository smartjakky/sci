from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData
from collections import OrderedDict


class MigrateManager(object):

    def __init__(self, from_db_uri, to_db_uri, migrate_tables, **kwargs):
        self.migrate_tables = migrate_tables

        self.from_db = create_engine(from_db_uri)
        self.from_metadata = MetaData(bind=self.from_db, reflect=True, schema=kwargs.get('from_schema', None))
        self.from_session = sessionmaker(bind=self.from_db)()

        self.to_db = create_engine(to_db_uri)
        self.to_metadata = MetaData(bind=self.to_db, schema=kwargs.get('to_schema', None))
        self.to_session = sessionmaker(bind=self.to_db)()

    def init_to_metadata(self):
        tables = OrderedDict()
        for table_name in self.migrate_tables:
            table = self.from_metadata.tables[table_name]
            tables[table_name] = table
        self.to_metadata.tables = tables

    def drop_table(self):
        self.init_to_metadata()
        self.to_metadata.drop_all(bind=self.to_db)

    def create_table(self):
        self.init_to_metadata()
        print(self.to_metadata.create_all(bind=self.to_db))

    def insert_data(self):
        for table_name in self.migrate_tables:
            table = self.to_metadata.tables[table_name]
            results = self.from_session.query(table).all()
            table.metadata = self.to_metadata
            table.schema = self.to_metadata.schema
            print(results)
            for result in results:
                print(self.to_db.execute(table.insert().values(result)))


if __name__ == '__main__':
    from_uri = 'postgresql://postgres:postgres@10.122.27.44/postgres'
    to_uri = 'hana://lidm1:lidm1(SCI)@10.122.13.22:30353'
    to_schema = 'LIMD1'
    migrate_tables = ['ab_user', 'ab_role', 'ab_user_role']
    mm = MigrateManager(from_uri, to_uri, migrate_tables, to_schema=to_schema)
    mm.create_table()
    mm.insert_data()
