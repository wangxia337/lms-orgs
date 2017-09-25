import json

import falcon
import objectpath


class Orgs(object):
    def on_get(self, request, response):
        keywords = request.get_param('keywords') or ''
        with open('asserts/orgs.json') as json_data:
            data = json.load(json_data)
        tree_obj = objectpath.Tree(data)
        if keywords:
            result = tuple(tree_obj.execute(
                "$.orgs[str({}) in @.orgName or str({}) in join(@.keywords)]".format(keywords, keywords)))
        else:
            result = tuple(tree_obj.execute("$.orgs.*"))

        response.status = falcon.HTTP_200
        response.body = json.dumps({'results': result}, ensure_ascii=False)
