package com.rnl.rest_n_link_demo;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@RestController
public class controller_rnl {

    @Autowired
    private rnlApiService apiService;

    @GetMapping("/nuevo_token_auth")
    @ResponseBody
    public String getRNL() {
        String respuesta = apiService.getTokenBearer();
        return respuesta;
    }

    @GetMapping("/mis_datos")
    @ResponseBody
    public String getMisDatos() {
        String respuesta = apiService.getClienteInfo();
        return respuesta;
    }    


    
}
