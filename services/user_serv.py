import data.db_session as db_session
from data.info import Info


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(Info).count()