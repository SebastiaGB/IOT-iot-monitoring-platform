# coding: utf-8

import requests
import warnings
import os

# Ignorar advertencies SSL
warnings.filterwarnings("ignore")

# Credencials
username = os.environ.get("CAMERA_USERNAME", "<CAMERA_USERNAME>")
password = os.environ.get("CAMERA_PASSWORD", "<CAMERA_PASSWORD>")

# URL de la càmara Bosch IP y comanda para obtenir els valores de els contadores IVA
camera_host = os.environ.get("CAMERA_HOST", "<CAMERA_HOST_OR_IP>")
url_reset_counters = f"https://{camera_host}/rcp.xml?command=0x0b4a&type=P_OCTET&direction=WRITE"

# Mètode per a reiniciar els contadors
def reset_counters(url):
    try:
        # Enviar solicitud HTTPS GET amb credencials
        response = requests.get(url, auth=(username, password), verify=False)
        # Verificar si la solicitud té èxit
        if response.status_code == 200:
            # Retornar la resposta en binari
            return response.content
    except requests.exceptions.ConnectionError as e:
        e

# Executar mètode
reset_counters(url_reset_counters)
