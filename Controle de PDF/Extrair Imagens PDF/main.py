from pikepdf import Pdf, PdfImage

arquivo = Pdf.open("tubarao.pdf")

for pagina in arquivo.pages:
    for nome, imagem in pagina.images.items():
        imagem_salvar = PdfImage(imagem)
        imagem_salvar.extract_to(fileprefix=f"Imagens/{nome}")
