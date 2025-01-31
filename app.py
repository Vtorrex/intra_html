from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def obtener_cotizacion():
    url = "https://www.cambioschaco.com.py/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        cotizacion = soup.find("div", class_="table-exchange-content")
        return cotizacion.text if cotizacion else "No disponible"
    return "Error al obtener cotización"

@app.route("/")
def index():
    cotizacion = obtener_cotizacion()
    return render_template("index.html", cotizacion=cotizacion)

if __name__ == "__main__":
    app.run(debug=True)
