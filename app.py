import flask
import os
import sys
import db_session as db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)

"""
This is the revised app as of August 10, 2019. the change is an effort to professionalize the site.
"""

def main():
    register_blueprints()
    setup_db()
    app.run('127.0.0.1', debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'drop.sqlite')

    db_session.glob_init(db_file)


def register_blueprints():
    from views import home_views
    from views import about_views
    from views import archive_views
    from views import drop_views
    from views import account_views    
    from views import cms_views
    
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(about_views.blueprint)
    app.register_blueprint(archive_views.blueprint)
    app.register_blueprint(drop_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__=='__main__':
    main()
