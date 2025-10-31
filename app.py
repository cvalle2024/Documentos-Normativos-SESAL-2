import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Documentos Normativos – SESAL-2", layout="wide")
st.title("Documentos Normativos – SESAL-2")

html_path = Path("index_2.html")
if html_path.exists():
    st.components.v1.html(html_path.read_text(encoding="utf-8"), height=900, scrolling=True)
else:
    st.error("No se encontró index_2.html en la raíz del repositorio.")

# (Opcional) listar archivos de la carpeta Documentos
docs_dir = Path("Documentos")
if docs_dir.exists():
    st.subheader("Archivos en /Documentos")
    for p in sorted(docs_dir.rglob("*")):
        if p.is_file():
            st.download_button(f"Descargar {p.name}", p.read_bytes(), file_name=p.name)
