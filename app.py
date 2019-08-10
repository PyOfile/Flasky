import flask
import os
#import db_session as db_session


app = flask.Flask(__name__)

"""
This is the revised app as of july 30, 2019. the change is an effort to professionalize the site.
"""

def main():
    register_blueprints_a()
    register_blueprints_b()
    register_blueprints_c()
    register_blueprints_d()
    setup_db()
    app.run('127.0.0.1', debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'drop.sqlite')

#db_session.glob_init(db_file)


def register_blueprints_a():
    from views import home_views
    app.register_blueprint(home_views.blueprint)


def register_blueprints_b():
    from views import drop_views
    app.register_blueprint(drop_views.blueprint)


def register_blueprints_c():
    from views import account_views
    app.register_blueprint(account_views.blueprint)


def register_blueprints_d():
    from views import cms_views
    app.register_blueprint(cms_views.blueprint)



if __name__=='__main__':
    main()
