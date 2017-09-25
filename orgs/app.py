import falcon

from orgs.model import Orgs

api = application = falcon.API()

api.add_route('/orgs', Orgs())
