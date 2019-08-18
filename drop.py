import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
from mod import SqlAlchemyBase
"""
First time sqlalchemy 08/18/19
"""
class Drop(SqlAlchemyBase):
    __tablename__ = "drop"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)


    package_id = sa.Column(sa.String, sa.ForeignKey("drop.id"))
    drop = orm.relation('Drop')


def __rep__(self):
    return '<drop {}>'.format(self.id)