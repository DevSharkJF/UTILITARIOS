# Extrai o texto e a tabela de um PDF
import pdfplumber

def extrair_texto(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto_completo = ''
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
        return texto_completo

def extrair_tabelas(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tabelas = []
        for pagina in pdf.pages:
            tabelas += pagina.extract_tables()
        return tabelas

if __name__ == "__main__":
    caminho_pdf = ".\Extrair Texto e Tabela\Pdfp Lumber\pdf_nome.pdf"
    
    texto = extrair_texto(caminho_pdf)
    print("\nTexto extraído do PDF:")
    print(f'{texto}\n')

    tabelas = extrair_tabelas(caminho_pdf)
    print("\nTabelas extraídas do PDF:")
    for tabela in tabelas:
        for linha in tabela:
            print(linha)
