import falcon, json, config, requests

class mis_datos:
    def on_get(req, resp):
        url = config.REST_N_LINK_API_SERVER + "/api/v1/auth/cliente"
        header = {
            "Authorization" : "Bearer " + config.REST_N_LINK_AUTH_TOKEN
        }

        response = requests.request("GET", url, headers=header)

        if response.status_code == 200:
            data = response.json()
            resp.status = 200
            resp.body = json.dumps(data)
        else:
            resp.status = response.status_code
            resp.body = json.dumps({
                'error': 'Failed to fetch data from the API',
                'api_response': response.json()
            })

        
class new_token:
    def on_get(req, resp):
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
            resp.status = 200
            resp.body = json.dumps(data)
        else:
            resp.status = response.status_code
            resp.body = json.dumps({
                'error': 'Failed to fetch data from the API',
                'api_response': response.json()
            })
        