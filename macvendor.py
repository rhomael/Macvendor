import streamlit as st
import requests

def get_mac_vendor(mac_address):
    url = 'https://api.macvendors.com/'
    response = requests.get(url + mac_address)
    if response.status_code == 200:
        return response.text
    else:
        return 'Não foi possível obter o fabricante do MAC address ❌.'

# Configuração da página do Streamlit
st.set_page_config(
    page_title="MAC Vendor Lookup",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilo moderno padrão Apple
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5f7;
        font-family: -apple-system, BlinkMacSystemFont, 'San Francisco', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #1d1d1f;
    }
    .stTextInput > div > input {
        border: 1px solid #d2d2d7;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #007aff;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #005bb5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título da aplicação
st.title("🔍 MAC Vendor Lookup")

# Adicionando o markdown minimalista
st.markdown("Desenvolvido por **Rhomael Pinheiro**®.")

# Entrada do usuário para o MAC Address
mac_address = st.text_input("Digite o MAC Address que deseja verificar:")

# Botão para buscar o fabricante
def buscar_fabricante():
    if mac_address:
        fabricante = get_mac_vendor(mac_address)
        st.success(f"Fabricante do MAC address ➡ {mac_address}: {fabricante}")
    else:
        st.error("Por favor, insira um MAC Address válido.")

st.button("Buscar Fabricante", on_click=buscar_fabricante)
