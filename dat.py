import sqlalchemy as sa

from mod import SqlAlchemyBase
"""
First time sqlalchemy 08/09/19
"""
class Drop(SqlAlchemyBase):
    __tablename__ = "drop"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    create_date = sa.Column(sa.DateTime)


def __rep__(self):
    return '<drop {}>'.format(self.id)
