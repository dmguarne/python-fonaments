import requests

try:
    response = requests.get("http://api.open-notify.org/iss-now.json") ## Fa la petició al servidor i l'emmagatzema en text a la variable response.
    if response.status_code == 200: ## Si la resposta del servidor és positiva, executa el codi.
        dades = response.json() ## Converteix el text de la resposta del servidor a Python.
        print(f"La latitud és {dades['iss_position']['latitude']} i la longitud és {dades['iss_position']['longitude']}") ## Imprimeix les claus latitud i longitud.
    else:
        print(response.status_code) ## Si la resposta del servidor no és 200, informa del codi de resposta.
except ConnectionError: ## Si la connexió amb el servidor ha fallat, informa.
    print("No s'ha pogut connectar amb el servidor")