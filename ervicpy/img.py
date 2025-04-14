import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def descargar_imagenes(url, carpeta_destino="imagenes_descargadas"):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    headers = {"User-Agent": "Mozilla/5.0"}
    respuesta = requests.get(url, headers=headers)
    
    if respuesta.status_code != 200:
        print(f"Error al acceder a {url} (Código: {respuesta.status_code})")
        return

    soup = BeautifulSoup(respuesta.text, "html.parser")
    imagenes = soup.find_all("img")

    print(f"🔍 Encontradas {len(imagenes)} imágenes. Descargando...")

    for i, img in enumerate(imagenes):
        src = img.get("src")
        if not src:
            continue

        img_url = urljoin(url, src)
        ext = os.path.splitext(img_url)[-1].lower()
        if ext not in [".jpg", ".jpeg", ".png", ".gif"]:
            ext = ".jpg"  # Por si no tiene extensión válida, se fuerza a .jpg

        try:
            img_data = requests.get(img_url, headers=headers).content
            nombre_archivo = os.path.join(carpeta_destino, f"imagen_{i+1}{ext}")
            with open(nombre_archivo, "wb") as f:
                f.write(img_data)
            print(f"✅ Guardada: {nombre_archivo}")
        except Exception as e:
            print(f"❌ Error al descargar {img_url}: {e}")

# 👉 URL fija (puedes cambiarla por la que quieras)
url = "http://komsik.50webs.com/Gunbound/index.html"
descargar_imagenes(url)
