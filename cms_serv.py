fake_db = {
    '/company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...',
    },
    '/company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about company employees ...',
    },
}

"""
cms server that will direct traffic to 404 if we make sure to add them here.
"""


def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = '/' + url.lstrip('/')

    page = fake_db.get(url, {})
    return page
