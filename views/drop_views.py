import flask
from vi_mod import response

"""
This is the revised app as off july 30, 2019. the chahnge is an effort to proffessionalize the site.
"""

blueprint = flask.Blueprint('drop', __name__, template_folder='templates')


@blueprint.route('/Drop-Form')
@response(template_file='form/dropform.html')
def fo():
    return {}


@blueprint.route('/dropform/login', methods=['GET'])
@response(template_file='dropform/login.html')
def log_get():
    return {}


@blueprint.route('/dropform/login', methods=['POST'])
@response(template_file='account/login.html')
def log_post():
    return {}


@blueprint.route('/dropform/logout')
def out():
    return {}
