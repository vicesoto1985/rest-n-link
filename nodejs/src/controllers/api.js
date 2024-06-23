import axios from "axios"
import {
    REST_N_LINK_API_SERVER,
    REST_N_LINK_CLIENTE_ID,
    REST_N_LINK_CONTACTO_ID,
    REST_N_LINK_API_KEY,
    REST_N_LINK_AUTH_TOKEN
} from "../config.js"
import { response } from "express"


export const get_cliente_data = async (req, res)=>{
    try{
        const url = REST_N_LINK_API_SERVER + "/api/v1/auth/cliente"

        const headers = {
            "Authorization" : "Bearer " + REST_N_LINK_AUTH_TOKEN
        }
    
        await axios.get(url, {
            headers
            })
            .then( response=>{
                res.status(response.status).send( response.data )
            }).catch(error =>{
                res.status(error.response.status).send( error.response.data )
            })
    }catch(e){
        console.log("Error en ejecución: ", e)
        res.status(500).send("Error en ejecución")
    }
    
}

export const get_token = async (req, res)=>{
    try{
        const url = REST_N_LINK_API_SERVER + "/api/v1/auth/access-token"

        const bodyJson = {
            "cliente_id" : REST_N_LINK_CLIENTE_ID,
            "contacto_id" : REST_N_LINK_CONTACTO_ID,
            "api_key" : REST_N_LINK_API_KEY        
        }
    
        await axios.post(url, bodyJson)
            .then( response=>{
                res.status(response.status).send( response.data )
            }).catch(error =>{
                res.status(error.response.status).send( error.response.data )
            })
    }catch(e){
        console.log("Error en ejecución: ", e)
        res.status(500).send("Error en ejecución")
    }
    
    

    

}