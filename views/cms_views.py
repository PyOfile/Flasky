import flask
from vi_mod import response
import cms_serv as cms_service

"""
V 001
"""

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cm(full_url: str):
    print("Getting CMS page for {}".format(full_url))

    page = cms_service.get_page(full_url)
    if not page:
        return flask.abort(404)

    return page

