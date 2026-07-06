# UTILITÁRIOS
Alguns códigos que foram usados para aprimoramento de conhecimento e para fins educacionais.

**OBS:** Sempre verifique e altere os caminhos do diretório, para evitar erros.

# Controle de PDF
Opções de extração, download e geração de PDF's.

## Extrair Imagens
Extrai as imagens de um pdf.

Para utilizar é necessário instalar a biblioteca pikepdf:

    pip install pikepdf

Link de download e documentação:

* https://pypi.org/project/pikepdf/ 
* https://pikepdf.readthedocs.io/en/latest/

## Extrair Texto e Tabela
Faz extração de textos e tabelas, dividido em duas bibliotecas, a ``pdfp lumber`` e ``pypdf``.

### Pdfp Lumber
Está dividido em três arquivos, um que extrai:

* Somente Tabelas
* Somente Texto
* Tabela e Texto

Instalação da biblioteca:

    pip install pdfplumber

Link para consulta e documentação:

    https://www.pdfplumber.com

### PyPDF
Faz extração somente de textos.

Instalação da Biblioteca:

    pip install pypdf

Link de documentação:
    https://pypdf.readthedocs.io/en/stable/

# Download de PDF
Faz o download de um PDF que está bloqueado ou em um determinado site

**Download de PDF:**
* Abra o pdf em uma página única.
* Rode o scroll do mouse da primeira até a última página.
* Mantenha uma velocidade média, em que todas as páginas do pdf sejam carregadas.
* Abra o modo desenvolvedor do chrome (F12) ou click com botão direito e selecione 'Inspecionar elemento'.
* Selecione a aba 'Console' e cole o script.
* Não reduza o tamanho da janela, isso afetará o formato do pdf.
* Aguarde as imagens serem adicionadas a um novo PDF.

**ERROS:**
* Caso o DevTools esteja instalado e rejeitando o script, digite no console "permitir colar" ou em inglês "allow paste".<br>
    Caso o erro persista, desabilite o DevTools.

* Vários PDFs em uma pasta só, pode acarretar no download de partes de outros PDFs.<br>
    Para contornar isso, deixe o PDF desejado em apenas uma pasta só, para evitar esse conflito.

* É normal que o script faça download de imagens brancas, o que aumenta a quantidade de páginas.<br>
    Ex: Pdf de 180 pag, pode ir para 183.