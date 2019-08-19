import flask
from vmod.vi_mod import response

"""
This is the revised app as of july 29, 2019. the change is an effort to professionalize the site.
"""

blueprint = flask.Blueprint('about', __name__, template_folder='templates')


@blueprint.route('/About')
@response(template_file='about/about.html')
def ab():
    return {}
