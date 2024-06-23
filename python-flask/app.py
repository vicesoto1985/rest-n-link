from flask import Flask, Blueprint
from routers.router_api_ import api_connect


app = Flask(__name__)

app.register_blueprint(api_connect, url_prefix='/rest-n-link')

if __name__ == "__main__":
    V_HOST = "0.0.0.0"
    V_PORT = 5555
    V_DEBUG = True

    app.run(host=V_HOST, port=V_PORT, debug=V_DEBUG)