import streamlit as st
import whisper
import os

st.title("Transcrição Automática de Vídeo/Áudio com Whisper")

uploaded_file = st.file_uploader(
    "Selecione um vídeo / áudio para transcrição",
    type=["mp4", "mp3", "wav", "m4a", "mpeg4"]
)

st.sidebar.title("Opções de Transcrição")
timestamp_option = st.sidebar._selectbox(
    "Exibir timestamps na transcrição?",
    ["Sim", "Não"]
)
add_timestamps = timestamp_option =="Sim"

model_name = st.sidebar.selectbox(
    "Modelo Whisper",
    ["tiny", "base", "small", "medium", "large"],
    index=2
)

language = st.sidebar._selectbox(
    "Idioma do áudio",
    ["auto", "pt", "en", "es", "fr", "de"],
    index=0,
    help="Defina o idioma do áudio para melhorar a transcrição (auto detecção)"
)