import falcon, json, config, requests
from routers.router_api import mis_datos, new_token

app = falcon.App()

app.add_route("/rest-n-link/mis_datos", mis_datos)
app.add_route("/rest-n-link/nuevo_token_auth", new_token)


if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    httpd.serve_forever()