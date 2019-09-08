import sqlalchemy as sa
import datetime
import sqlalchemy.orm as orm
from data.mod import SqlAlchemyBase
"""
First time sqlalchemy 08/18/19
"""
class Info(SqlAlchemyBase):
    __tablename__ = "info"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # example entries
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
