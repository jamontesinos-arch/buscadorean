# 🔍 Buscador Automático de Productos por EAN

Una herramienta web sencilla y directa para obtener el **Nombre del Producto** y su **Información** a partir de una lista de códigos EAN-13. 

Diseñada para ser utilizada por cualquier persona de forma rápida, sin necesidad de instalaciones, conocimientos técnicos ni configuración de APIs.

## ✨ Características Principales

* **Búsqueda Masiva:** Pega una lista de EANs directamente desde Excel o Google Sheets.
* **Cero Configuración:** No requiere registros, API Keys ni sistemas complejos.
* **Motor Anti-Bloqueos:** Utiliza un sistema de rastreo optimizado (Yahoo Search) para evadir las restricciones de búsqueda y obtener resultados fiables sin interrupciones.
* **Exportación a Excel:** Descarga todos los resultados obtenidos con un solo clic en formato CSV, listos para abrir en tu hoja de cálculo.

## 🚀 Cómo usar esta herramienta

1. **Accede a la web:** Entra en el enlace proporcionado de Streamlit.
2. **Introduce tus códigos:** Pega los EAN de 13 dígitos en el cuadro de texto principal (uno por línea o separados por comas).
3. **Inicia la Búsqueda:** Pulsa el botón azul "Iniciar Búsqueda". El sistema procesará cada código con una pequeña pausa de seguridad de 2 segundos.
4. **Descarga los datos:** Cuando la barra de progreso termine, aparecerá un botón para descargar un archivo `.csv` con todos tus resultados.

## 🛠️ Archivos del Proyecto

* `app.py`: Contiene el motor de búsqueda y la interfaz visual generada con Streamlit.
* `requirements.txt`: Lista de librerías necesarias para que el servidor funcione (`streamlit`, `requests`, `beautifulsoup4`, `pandas`).

---
Desarrollado con 🐍 Python y Streamlit para facilitar el trabajo diario.