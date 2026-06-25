# Extrai o texto do PDF
from pypdf import PdfReader

def ler_pdf(caminho_pdf: str) -> str:
    leitor = PdfReader(caminho_pdf)
    texto = ""

    for pagina in leitor.pages:
        texto += pagina.extract_text().strip() or ""
    return texto

conteudo = ler_pdf(".\Extração de Pdf\pdf_nome.pdf")
print(conteudo)
