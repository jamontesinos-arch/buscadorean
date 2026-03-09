import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

# Configuración de la interfaz
st.set_page_config(page_title="Buscador de EANs Tentacool", page_icon="🔍")

# 👇 SOLUCIÓN: Forzamos la conexión segura con https:// 👇
st.image("tentacool.jpg", width=100)

st.title("🔍 Buscador de Productos por EAN Tentacool")
st.markdown("""
Pega tu lista de códigos EAN abajo (uno por línea). 
Esta herramienta buscará el nombre y el MPN en internet automáticamente.
""")

# Motor de búsqueda (Yahoo/Bing index)
def buscar_producto(ean):
    url = f"https://es.search.yahoo.com/search?p={ean}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Localizamos el primer resultado orgánico
            resultado = soup.find('div', class_=lambda c: c and 'algo' in c)
            if resultado:
                titulo_tag = resultado.find('h3')
                desc_tag = resultado.find('div', class_='compText')
                
                titulo = titulo_tag.text.strip() if titulo_tag else "Título no encontrado"
                descripcion = desc_tag.text.strip() if desc_tag else "Sin descripción"
                return {"ean": ean, "status": "ok", "nombre": titulo, "info": descripcion[:150]}
            return {"ean": ean, "status": "error", "msg": "No se encontraron resultados"}
        return {"ean": ean, "status": "error", "msg": f"Error de conexión ({response.status_code})"}
    except Exception as e:
        return {"ean": ean, "status": "error", "msg": str(e)}

# Interfaz de usuario
eans_input = st.text_area("Lista de EANs:", height=200, placeholder="4718755097362\n4711121632525")

if st.button("Iniciar Búsqueda", type="primary"):
    if not eans_input.strip():
        st.warning("⚠️ Introduce al menos un EAN.")
    else:
        # Limpieza de datos
        eans = [e.strip() for e in eans_input.replace(',', '\n').split('\n') if e.strip()]
        st.info(f"Procesando {len(eans)} productos...")
        
        for ean in eans:
            res = buscar_producto(ean)
            if res["status"] == "ok":
                st.success(f"**EAN: {res['ean']}**\n\n**Nombre:** {res['nombre']}\n\n**Info:** {res['info']}...")
            else:
                st.error(f"**EAN: {res['ean']}** - {res['msg']}")
            
            # Pausa para evitar bloqueos
            time.sleep(2)
        st.balloons()




