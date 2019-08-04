import flask
from vi_mod import response

"""
This is the revised app as off july 29, 2019. the chahnge is an effort to proffessionalize the site.
"""

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/Account')
@response(template_file='pays/account.html')
def ac():
    return {}


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/consult.html')
def reg_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/consult.html')
def reg_post():
    return {}
