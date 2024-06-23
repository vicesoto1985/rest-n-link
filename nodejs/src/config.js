import {config} from 'dotenv'
config()

export const REST_N_LINK_API_SERVER = process.env.REST_N_LINK_API_SERVER || "https://api.restnlink.com"
export const REST_N_LINK_CLIENTE_ID = process.env.REST_N_LINK_CLIENTE_ID || ""
export const REST_N_LINK_CONTACTO_ID = process.env.REST_N_LINK_CONTACTO_ID || ""
export const REST_N_LINK_API_KEY = process.env.REST_N_LINK_API_KEY || ""

export const REST_N_LINK_AUTH_TOKEN = process.env.REST_N_LINK_AUTH_TOKEN || ""
