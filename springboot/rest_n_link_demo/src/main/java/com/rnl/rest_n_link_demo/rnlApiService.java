package com.rnl.rest_n_link_demo;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.HttpServerErrorException;
import org.springframework.web.client.RestTemplate;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;

@Service
public class rnlApiService {
    @Autowired
    private RestTemplate restTemplate;

    @Value("${rest.n.link.api.server}")
    private String url;

    @Value("${rest.n.link.cliente.id}")
    private String cliente_id;

    @Value("${rest.n.link.contacto.id}")
    private String contacto_id;

    @Value("${rest.n.link.api.key}")
    private String api_key;

    @Value("${rest.n.link.auth.token}")
    private String auth_token;

    public String getTokenBearer(){

        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");

        Map<String, Object> body = new HashMap<>();
        body.put("cliente_id", cliente_id);
        body.put("contacto_id", contacto_id);
        body.put("api_key", api_key);

        HttpEntity<Map<String, Object>> entity = new HttpEntity<>(body, headers);

        try {
            ResponseEntity<String> response = restTemplate.exchange(url + "api/v1/auth/access-token", HttpMethod.POST, entity, String.class);
            return response.getBody();
        } catch (HttpClientErrorException e) {
            if (e.getStatusCode().is4xxClientError()) {
                return e.getStatusCode() + " : " + e.getMessage();
            } else {
                return e.getStatusCode().toString();
            }
        } catch (HttpServerErrorException e) {
            return e.getStatusCode().toString();
        } catch (Exception e) {
            return e.getMessage();
        }    
    }


    public String getClienteInfo(){
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");
        headers.set("Authorization", "Bearer "+auth_token);

        HttpEntity<Map<String, Object>> entity = new HttpEntity<>(null, headers);

        try {
            ResponseEntity<String> response = restTemplate.exchange(url + "/api/v1/auth/cliente", HttpMethod.GET, entity, String.class);
            return response.getBody();
        } catch (HttpClientErrorException e) {
            if (e.getStatusCode().is4xxClientError()) {
                return e.getStatusCode() + " : " + e.getMessage();
            } else {
                return e.getStatusCode().toString();
            }
        } catch (HttpServerErrorException e) {
            return e.getStatusCode().toString();
        } catch (Exception e) {
            return e.getMessage();
        }    
    }    

}
