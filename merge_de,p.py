from sci.models.superset import SqlaTableFilter
from superset import db

#     id = Column(Integer, Sequence(__tablename__ + '_id_seq'), primary_key=True)
#     table_id = Column(Integer, ForeignKey('sqla_tables.id'))
#     table = relationship(
#         'SqlaTable',
#         backref=backref('table_filter', cascade='all, delete-orphan'),
#         foreign_keys=[table_id])
#     title = Column('title', String(64))
#     input_type = Column('input_type', String(30))
#     select_mode = Column('select_mode', String(20), default='multiple')
#     columns = Column('columns', String(100), nullable=False)
#     is_require = Column('is_require', Boolean, default=False, nullable=False)
#     seq = Column('seq', Integer)
#     start_value = Column(String(30))
#     end_value = Column(String(30))
#     min_value = Column(String(30))
#     max_value = Column(String(30))
#     min_range = Column(String(30))
#     max_range = Column(String(30))
#     default_value = Column(String(100))
#     default_op = Column(String(30))
#     slide_step = Column(String(30))
#     col_sort = Column(String(20))

db.session.add(SqlaTableFilter(
    table_id=202,
    title="Version",
    input_type="dropdown_list",
    select_mode="single",
    columns="version",
    col_sort="version",
    is_require=True,
    seq=1,
    default_value="top(1)",
))
db.session.add(SqlaTableFilter(
    table_id=202,
    title="Product",
    input_type="dropdown_list",
    select_mode="single",
    columns="product",
    col_sort="product",
    is_require=False,
    seq=2,
    default_value="top(1)",
))
db.session.add(SqlaTableFilter(
    table_id=202,
    title="Geo",
    input_type="dropdown_list",
    select_mode="single",
    columns="geo",
    col_sort="geo",
    is_require=False,
    seq=3,
    default_value="top(1)",
))
db.session.add(SqlaTableFilter(
    table_id=202,
    title="Country",
    input_type="dropdown_list",
    select_mode="single",
    columns="country",
    col_sort="country",
    is_require=False,
    seq=4,
    default_value="top(1)",
))
