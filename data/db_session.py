import sqlalchemy as sa 
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data.mod import SqlAlchemyBase

"""
This is where the db majic happens. totally learning this. 
"""

__factory = None

def glob_init(db_file:str):
    global __factory


    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file!")

    conn_str = 'sqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(conn_str))

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.__models
    
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()