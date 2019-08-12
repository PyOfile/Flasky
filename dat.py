import sqlalchemy as sa

from mod import SqlAlchemyBase
"""
First time sqlalchemy 08/09/19, this is where we need to model the data from the dropform.html page. We need to make sure they match up right.
"""
class Drop(SqlAlchemyBase):
    __tablename__ = "drop"
    
    id = sa.Column(sa.Integer, primary_key=True)
    create_date = sa.Column(sa.DateTime, index=True)
    

def __rep__(self):
    return '<drop {}>'.format(self.id)
