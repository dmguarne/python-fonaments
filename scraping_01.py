import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

if response.status_code == 200:
    dades = response.json()
    print(f"La latitud és {dades['iss_position']['latitude']} i la longitud és {dades['iss_position']['longitude']}")
else:
    print(response.status_code)
