import requests
from bs4 import BeautifulSoup

# URL de la página que quieres extraer
url = "https://www.cambioschaco.com.py/"

# Simular un navegador para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Hacer la petición a la página
response = requests.get(url, headers=headers)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Analizar el HTML de la página
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar el elemento con la clase "cotizacion"
    cotizacion = soup.find("div", class_="table-exchange-content")

    # Verificar si se encontró la cotización
    if cotizacion:
        print("Cotización actual:", cotizacion.text)
    else:
        print("No se encontró la cotización.")
else:
    print(f"Error al acceder a la página: {response.status_code}")
