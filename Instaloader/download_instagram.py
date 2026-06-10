import instaloader
import os

loader = instaloader.Instaloader(dirname_pattern="Instaloader/{target}")
# loader = instaloader.Instaloader(
#     download_comments=False,
#     download_geotags=False,
#     download_pictures=False,
#     download_video_thumbnails=False,
#     save_metadata=False
# )
post_url = input("Informe a URL do Post: ")
shortcode = post_url.split("/")[-2]

try:
    loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target= "Download Post")
    print("Download concluído!")
except Exception as e:
    print(f"Erro ao fazer download: {e}")

# Outro Método para fazer:
"""
import instaloader
import os
loader = instaloader.Instaloader()
# loader = instaloader.Instaloader(
#     download_comments=False,
#     download_geotags=False,
#     download_pictures=False,
#     download_video_thumbnails=False,
#     save_metadata=False
# )
post_url = input("Informe a URL do Post: ")
shortcode = post_url.split("/")[-2]

destino = "Instaloader"
os.makedirs(destino, exist_ok=True)
os.chdir(destino)

try:
    loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target= "Download Post")
    print("Download concluído!")
except Exception as e:
    print(f"Erro ao fazer download: {e}")
"""
