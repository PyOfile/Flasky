import flask
from vmod.vi_mod import response
import services.user_serv as user_service

"""
This is the revised app as of july 29, 2019. the change is an effort to professionalize the site.
"""

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='index/index.html')
def ix():
    return {
        'user_count': user_service.get_user_count(),
    }


@blueprint.route('/login', methods=['GET'])
@response(template_file='/login.html')
def log_get():
    return {}


@blueprint.route('/login', methods=['POST'])
@response(template_file='account/login.html')
def log_post():
    return {}


@blueprint.route('/logout')
def out():
    return {}

