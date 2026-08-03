from rembg import remove
from PIL import Image

input = Image.open("arquivo.extensao")
output = remove(input)
output.save("novo_arquivo.extensao")