import instaloader
import os
import time

loader = instaloader.Instaloader(dirname_pattern="Instaloader/{target}")
os.system('cls')
post_url = input("🔗 Informe a URL do Post: ")
shortcode = post_url.split("/")[-2]

try:
    print("⏳ Baixando o Conteúdo...")
    loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target= "Download Post")
    os.system('cls')
    print("✅ Download concluído ✅\n" 
        "Verifique a pasta Download Post"
    )
except Exception as e:
    print(f"❌Erro ao fazer download: {e}")

# Outro Método para fazer:
"""
loader = instaloader.Instaloader(
    download_comments=True,
    download_geotags=True,
    download_pictures=True,
    download_video_thumbnails=True,
    save_metadata=True,
)
post_url = input("🔗 Informe a URL do Post: ")
shortcode = post_url.split("/")[-2]

destino = "Instaloader"
os.makedirs(destino, exist_ok=True)
os.chdir(destino)

try:
    print("⏳ Baixando o Conteúdo...")
    loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target= "Download Post")
    print("✅ Download concluído ✅\n" 
        "Verifique a pasta Download Post"
    )
except Exception as e:
    print(f"❌Erro ao fazer download: {e}")
"""
