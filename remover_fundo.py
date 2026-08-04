from rembg import remove
from PIL import Image
from time import sleep

print("\n"
    "---------------------INICIANDO PROGRAMA---------------------"
    "\n"
)
input = Image.open("foto.extensao")
print("🖋️  PREPARANDO PARA EDITAR O ARQUIVO...")
sleep(2)
print("-------------------------------------------------")
output = remove(input)
print("🏜️  REMOVENDO O FUNDO DA IMAGEM...")
sleep(2)
print("-------------------------------------------------")
output.save("nova_foto.png")
print(
    "✅ CONCLUÍDO \n"
    "⬇️  VERIFIQUE A NOVA IMAGEM COM NOME 'nova_foto.png'\n"
)