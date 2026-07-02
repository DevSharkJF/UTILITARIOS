from pytubefix import YouTube
import time
import os

os.system('cls')
link = input("🔗 Digite o link do Vídeo: ")
yt = YouTube(link)

destino = "./Download Audio/Áudios Baixados"
audio = yt.streams.filter(only_audio=True, file_extension="mp4", mime_type="audio/mp4").first()

print(f"⌛ Baixando áudio: {audio.title}")
audio_file = audio.download(filename=f"{audio.title}audio.mp4", output_path=destino)

time.sleep(1.5)
os.system('cls')
print("✅ Download Concluído")