import sqlalchemy as sa 
import sqlalchemy.orm as orm
from data.mod import SqlAlchemyBase

"""
This is where the db majic happens. totally learning this. 
"""

factory = None

def glob_init(db_file:str):
    global factory


    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file!")

    conn_str = 'sqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(conn_str))

    engine = sa.create_engine(conn_str, echo=False)
    actory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.__models
    
    SqlAlchemyBase.metadata.create_all(engine)
