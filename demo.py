import falcon

class ThingsResource(object):
    def on_get(self, req, resp):
        resp.status=falcon.HTTP_200
        resp.body=('\n two things awe me most,the starry sky'
                    'above me and the moral law within me.\n'
                    '\n'
                    '     ~Immanuel Kant\n\n')


app = falcon.API()
demo = ThingsResource()
app.add_route('/demo',demo)

# waitress-serve --port=8000 demo:app