import json
import os
import sys
import time
from typing import List, Optional, Dict

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

import data.db_session as db_session
from data.user_serv import Info


def main():
    init_db()
    session = db_session.create_session()
    user_count = session.query(Info).count()
    session.close()
    if user_count == 0:
        file_data = do_load_files()
        users = find_users(file_data)
    do_summary()


def do_summary():
    session = db_session.create_session()

    print("Final numbers:")
    print("Users: {:,}".format(session.query(Info).count()))


def do_load_files() -> List[dict]:
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../data/a100'))
    print("Loading files from {}".format(data_path))
    files = get_file_names(data_path)
    print("Found {:,} files, loading ...".format(len(files)), flush=True)
    time.sleep(.1)

    file_data = []
    sys.stderr.flush()
    sys.stdout.flush()
    print()
    return file_data


def find_users(data: List[dict]) -> dict:
    print("Discovering users...", flush=True)
    found_users = {}

    sys.stderr.flush()
    sys.stdout.flush()
    print()
    print("Discovered {:,} users".format(len(found_users)))
    print()

    return found_users


def get_email_and_name_from_text(name: str, email: str) -> dict:
    data = {}

    if not name or not email:
        return data

    emails = email.strip().lower().split(',')
    names = name
    if len(email) > 1:
        names = name.strip().split(',')

    for n, e in zip(names, emails):
        if not n or not e:
            continue

        data[e.strip()] = n.strip()

    return data


def load_file_data(filename: str) -> dict:
    try:
        with open(filename, 'r', encoding='utf-8') as fin:
            data = json.load(fin)
    except Exception as x:
        print("ERROR in file: {}, details: {}".format(filename, x), flush=True)
        raise

    return data


def try_int(text) -> int:
    try:
        return int(text)
    except:
        return 0


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


def get_file_names(data_path: str) -> List[str]:
    files = []
    for f in os.listdir(data_path):
        if f.endswith('.json'):
            files.append(
                os.path.abspath(os.path.join(data_path, f))
            )

    files.sort()
    return files


if __name__ == '__main__':
    main()