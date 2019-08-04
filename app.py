import flask

app = flask.Flask(__name__)

"""
This is the revised app as of july 30, 2019. the change is an effort to professionalize the site.
"""

def main():
    register_blueprints_a()
    register_blueprints_b()
    register_blueprints_c()
    app.run('127.0.0.1', debug=True)


def register_blueprints_a():
    from views import home_views
    app.register_blueprint(home_views.blueprint)


def register_blueprints_b():
    from views import drop_views
    app.register_blueprint(drop_views.blueprint)


def register_blueprints_c():
    from views import account_views
    app.register_blueprint(account_views.blueprint)


if __name__=='__main__':
    main()
