from pytubefix import YouTube
from pytubefix.cli import on_progress
import time
import os

url = input("🔗 Digite o link do Vídeo: ")
destino = "./Download Video/Vídeos Baixados"

yt = YouTube(url, on_progress_callback= on_progress)
print(f"⌛ Baixando vídeo: {yt.title}")

ys = yt.streams.get_highest_resolution()
ys.download(output_path=destino)

time.sleep(1.5)
os.system('cls')
print("✅ Download Concluído")