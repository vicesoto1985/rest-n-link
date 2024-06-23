import { Router } from "express";
import {get_cliente_data, get_token} from "../controllers/api.js"

const router = new Router()

router.get("/mis_datos", get_cliente_data)
router.get("/nuevo_token_auth", get_token)

export default router