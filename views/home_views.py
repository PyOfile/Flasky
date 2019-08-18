import flask
from vi_mod import response

"""
This is the revised app as of july 29, 2019. the change is an effort to professionalize the site.
"""

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='index/index.html')
def ix():
    return {}
