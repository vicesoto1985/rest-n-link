import os
from dotenv import load_dotenv
load_dotenv()
REST_N_LINK_API_SERVER = os.getenv('REST_N_LINK_API_SERVER', "")
REST_N_LINK_CLIENTE_ID = os.getenv('REST_N_LINK_CLIENTE_ID', "")
REST_N_LINK_CONTACTO_ID = os.getenv('REST_N_LINK_CONTACTO_ID', "")
REST_N_LINK_API_KEY = os.getenv('REST_N_LINK_API_KEY', "")
REST_N_LINK_AUTH_TOKEN = os.getenv('REST_N_LINK_AUTH_TOKEN', "")

