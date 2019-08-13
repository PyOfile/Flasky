import sqlalchemy as sa
import sqlalchemy.orm as orm
from mod import SqlAlchemyBase
"""
First time sqlalchemy 08/09/19
"""
class Drop(SqlAlchemyBase):
    __tablename__ = "drop"
    
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    created_date = sa.Column(sa.DateTime, index=True)


def __rep__(self):
    return '<drop {}>'.format(self.id)
