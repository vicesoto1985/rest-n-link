from flask import Blueprint, jsonify
import requests, config, json

api_connect = Blueprint('api_connect', __name__)

@api_connect.route('/mis_datos', methods=['GET'])
def get_users():

    url = config.REST_N_LINK_API_SERVER + "/api/v1/auth/cliente"
    header = {
        "Authorization" : "Bearer " + config.REST_N_LINK_AUTH_TOKEN
    }

    response = requests.request("GET", url, headers=header)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({
            'error': 'Failed to fetch data from the API',
            'api_response': response.json()
        }), response.status_code





@api_connect.route('/nuevo_token_auth', methods=['GET'])
def get_new_token():    
    url = config.REST_N_LINK_API_SERVER + "/api/v1/auth/access-token"
    header = {

    }
    payload = {
        "cliente_id" : config.REST_N_LINK_CLIENTE_ID,
        "contacto_id" : config.REST_N_LINK_CONTACTO_ID,
        "api_key" : config.REST_N_LINK_API_KEY
    }

    response = requests.request("POST", url, headers=header, json=payload)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({
            'error': 'Failed to fetch data from the API',
            'api_response': response.json()
        }), response.status_code


