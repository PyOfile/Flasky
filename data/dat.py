import sqlalchemy as sa

from mod import SqlAlchemyBase
"""
First time sqlalchemy 08/09/19
"""
class Drop(SqlAlchemyBase):
    __tablename__ = "drop"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    create_date = sa.Column(sa.DateTime)
    summery = sa.Column(sa.Sting)
    description = sa.Column(sa.Sting)
    
    home_page = sa.Column(sa.Sting)
    docs_url = sa.Column(sa.Sting)
    drop_url = sa.Column(sa.Sting)
    
    authur_name = sa.Column(sa.Sting)
    authur_email = sa.Column(sa.Sting)
    
    license = sa.Column(sa.Sting)
    
# maintainers
# releases
def __rep__(self):
    return '<drop {}>'.format(self.id)
