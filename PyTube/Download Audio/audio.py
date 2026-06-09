from pytubefix import YouTube
import time

#Adicione a URL do vídeo dentro das aspas:
link = ""
yt = YouTube(link)

destino = "./Download Audio/Áudios Baixados"
audio = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()

print(f"Baixando áudio: {audio.title}")
audio_file = audio.download(filename=f"{audio.title}audio.mp4", output_path=destino)

time.sleep(1.5)
print("Download Concluído!")