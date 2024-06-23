<?php
	$REST_N_LINK_API_SERVER = "https://api.restnlink.com";

	$REST_N_LINK_CLIENTE_ID = "";
	$REST_N_LINK_CONTACTO_ID = "";
	$REST_N_LINK_API_KEY = "";

	#TOKEN DE AUTORIZACIÓN CON VIGENCIA DE UNA HORA.
	#CONFIGURANDO LOS DATOS PREVIOS Y CORRIENDO EL SERVER, DEBES INGRESAR A ESTE LINK ( http://127.0.0.1:5555/rest-n-link/nuevo_token_auth ) PARA OBTENER EL TOKEN AUTH
	$REST_N_LINK_AUTH_TOKEN = "";	

	function getCurlResponse($URL, $METHOD, $HEADER, $BODY){
		$curl = curl_init($URL);
		curl_setopt($curl, CURLOPT_URL, $URL);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
		if($METHOD == "GET"){
			curl_setopt($curl, CURLOPT_HTTPGET, true);
		}else{
			curl_setopt($curl, CURLOPT_POST, true);
			curl_setopt($curl, CURLOPT_POSTFIELDS, $BODY);
		}
		
		curl_setopt($curl, CURLOPT_HEADER, false);
		curl_setopt($curl, CURLOPT_HTTPHEADER, $HEADER);
		
		
		curl_getinfo($curl, CURLINFO_HTTP_CODE);

		$response = curl_exec($curl);

		$Retorno = array(
			"code" => $http_code = curl_getinfo($curl, CURLINFO_HTTP_CODE),
			"message" => $response
		);
		curl_close($curl);
		return $Retorno;

	}


	if(isset($_GET["sec"])){
		switch($_GET["sec"]){
			case "mis-datos":
				$headers = array(
					"Authorization: Bearer $REST_N_LINK_AUTH_TOKEN",
				 );
				 
				 $Retorno = getCurlResponse($REST_N_LINK_API_SERVER."/api/v1/auth/cliente", "GET", $headers, "");
				 echo "Código respuesta: " . $Retorno["code"] . "<br>";
				 echo "Mensaje: ", $Retorno["message"];
				break;
			case "nuevo_token_auth":
				global $REST_N_LINK_CLIENTE_ID, $REST_N_LINK_CONTACTO_ID, $REST_N_LINK_API_KEY;
				$headers = array(
					"Accept: application/json"
				 );				
				$body = array(
					"cliente_id" => $REST_N_LINK_CLIENTE_ID,
					"contacto_id" => $REST_N_LINK_CONTACTO_ID,
					"api_key" => $REST_N_LINK_API_KEY
				);
				$Retorno = getCurlResponse($REST_N_LINK_API_SERVER."/api/v1/auth/access-token","POST", $headers, $body);
				echo "Código respuesta: " . $Retorno["code"] . "<br>";
				echo "Mensaje: ", $Retorno["message"];				
				break;
		}
	}
?>