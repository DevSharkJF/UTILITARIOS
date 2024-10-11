# import pytube
from pytubefix import YouTube
# from pytube import YouTube
import time

link = '' #Adicione a URL do vídeo dentro das aspas
yt = YouTube(link)

audio = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()

print(f"Baixando áudio: {audio.title}")
audio_file = audio.download(filename=f"{audio.title}audio.mp4")

time.sleep(3)

print("Download Concluído!")