from flask_appbuilder.security.sqla.models import Model
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String, Text

user_event = Table('user_event',
                   user_id=Column(Integer, ForeignKey('ab_user.id')),
                   event_id=Column(Integer, ForeignKey('event.id')),
                   user=relationship('User', ),
                   event=relationship('Event', ),
                   status=Column(String, default='new'),
                   )


class Event(Model):
    """事件通知模型"""
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    users = relationship('User', secondary=user_event, backref=backref('event'))
    templates = Column(Text, nullable=False)
    # priority = Column(Integer, nullable=True, default=0)

