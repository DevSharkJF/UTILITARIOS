# Extrai somente o texto de um PDF
import pdfplumber

def extrair_texto(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto_completo = ''

        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
        return texto_completo 

texto = extrair_texto(".\Extração de Pdf\Pdfp Lumber\pdf_nome.pdf")
print("\nTexto extraído do PDF:")
print(f'{texto}\n')