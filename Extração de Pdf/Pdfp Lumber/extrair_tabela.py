# Extrai Somente a tabela de um PDF
import pdfplumber
def extrair_tabelas(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tabelas = []
        for pagina in pdf.pages:
            tabelas += pagina.extract_tables()
        return tabelas

if __name__ == "__main__":

    caminho_pdf = ".\Extração de Pdf\Pdfp Lumber\pdf_nome.pdf"
    tabelas = extrair_tabelas(caminho_pdf)
    print("\nTabelas extraídas do PDF:")

    for tabela in tabelas:
        for linha in tabela:
            print(linha)

