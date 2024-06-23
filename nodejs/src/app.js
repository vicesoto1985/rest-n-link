import express from "express"
import bodyParser from "body-parser"
import axios from "axios"
import router_app from "./routers/router_api.js"

const app = express()

app.use(express.json())
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.use("/rest-n-link", router_app)



app.use((req, res, next)=>{
    res.status(404).json({
        message : "endpoint not found"
    })
});

app.listen(5555, ()=>{
    console.log("Servidor rest-n-link testing iniciado")
    console.log("http://127.0.0.1:5555")
})