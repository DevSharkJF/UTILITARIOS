# Código funciona, porém o arquivo do vídeo fica com resolução baixa
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


# Código Funciona, porém o arquivo do vídeo não está abrindo
from pytubefix import YouTube
from pytubefix.cli import on_progress
import time
import os
import subprocess

url = input("🔗 Digite o link do Vídeo: ")
destino = "./Download Video/Vídeos Baixados"

yt = YouTube(url, on_progress_callback=on_progress)
print(f"⌛ Baixando vídeo: {yt.title}")

video_stream = yt.streams.filter(adaptive=True, file_extension="mp4", res="1080p", fps=60).first()
audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first()

if not video_stream or not audio_stream:
    print("❌ Não foi possível encontrar vídeo 1080p60 ou áudio disponível.")
    exit(1)

video_path = video_stream.download(output_path=destino, filename_prefix="video_")
audio_path = audio_stream.download(output_path=destino, filename_prefix="audio_")
final_path = os.path.join(destino, f"{yt.title} - 1080p60.mp4")

subprocess.run([
    "ffmpeg", "-y",
    "-i", video_path,
    "-i", audio_path,
    "-c", "copy",
    final_path
], check=True)

os.remove(video_path)
os.remove(audio_path)

time.sleep(1.5)
os.system("cls")
print("✅ Download Concluído")