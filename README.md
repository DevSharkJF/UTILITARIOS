<center>

# UTILITÁRIOS
Alguns códigos que foram usados para aprimoramento de conhecimento e para fins educacionais.

**OBS:** Sempre verifique e altere os caminhos do diretório, para evitar erros.
</center>
<br>

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

## Download de PDF
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

## Gerar Documento
Cria um documento PDF, podendo alterar fonte, tamanho, formato entre outros.

No código foi desenvolvido um código que gera um recibo como exemplo.

Instalação da Biblioteca:

    pip install fpdf2 

Link de Documentação:

    https://py-pdf.github.io/fpdf2/Tutorial-pt.html

## Gerar Relatório
Captura os dados contidos no arquivo `manutencao.csv`, e gera um arquivo PDF individual baseado no conteúdo captado. 
No código foi usado um serviço de manutenção como exemplo.

Instalação das Bibliotecas:

    pip install pandas
    pip install reportlab

Links de Download e Documentação:
* https://pypi.org/project/reportlab/
* https://pypi.org/project/pandas/
<hr>

# Instaloader
O primeiro bloco de código, faz download geral do conteúdo na URL (foto, vídeo, thumb, legena).

O segundo bloco de código possui parâmetros de download, podendo adicionar o valor **FALSE** nos atributos que não deseja baixar.

Instalação da Biblioteca:

    pip install instaloader

Link da Documentação:
* https://instaloader.github.io

## InstaScrape
Instalação da Biblioteca:

    pip install instascrape

Links das Documentações:
* https://github.com/chris-greening/instascrape
* https://chris-greening.github.io/instascrape/

Faz o download do Rell, mas pode ser bloqueado caso tenha repetidas solicitações. Por conta disso, é necessário passar o session ID, devido às novas políticas do Instagram.

O SessionID muda sempre que a sessão é encerrada, por isso é importante fornecer o ID no momento em que estiver conectado.

O formato f-string é uma forma de inserir expressões Python dentro de Strings para formatação.

Para acessar o ``SESSION ID`` é necessário abrir o instagram no navegador, clicar com o botão direito do mouse na página e selecionar **Inspecionar** (ou pressionar F12). 
Em seguida, vá para a aba **Application** (*Aplicativo*), depois em **Storage** (*Armazenamento*) e clique em **Cookies** ou em **Armazenamento de Sessão**
Lá você encontrará o cookie chamado ``sessionid``, que é o valor que você precisa copiar e colar no código acima.
<hr>

# Ligações
Efetua ligações para outros números utilizando python

Instalação da Biblioteca:

    pip install twilio

É necessário criar uma conta no `twilio`:

    https://login.twilio.com/u/signup?state=hKFo2SBpd0hwS2Y0VnBGUm9Od3VwclFUcWljSzVGa181TmtlQaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFJYS3liS183NjB3LUNRTDhzOWRtaTluSVBQdGwwWlUzo2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks

Após criar a conta será possível obter o número do `sid`, ``token`` e ``número twilio.

Verifique o número de telefone para começar a usar, sendo liberado ligação gratuita para o número cadastrado, porém para outros números será necessário pagar.

A plataforma também libera para compra, diferentes tipos de números.
<hr>

# PyTube
<hr>

# QRCode
Cria QRCODE personalizado

Instalação das Bibliotecas:

    pip install qrcode
    pip install pillow

Link da Documentação: 
* https://pypi.org/project/qrcode/

``Obs:`` Para gerar um novo png, é necessário apagar o atual
<hr>

# ZapBot
Cria um bot que envia mensagens no whatsapp. O código irá abrir o Whatsapp Web para escanear o qrcode, após escanear aguarde o código enviar a mensagem para o contato

Instalação das Bibliotecas:

    pip install selenium
    pip install webdriver-manager 

Ao instalar o webdriver-manager, outras bibliotecas neecessárias já serão incluídas
--> Caso haja erro e as bibliotecas nao sejam instaladas, adicione elas manualmente

Bibliotecas e suas versões necessárias:

    attrs==23.2.0
    certifi==2024.2.2
    charset-normalizer==3.3.2
    h11==0.14.0
    idna==3.6
    outcome==1.3.0.post0
    packaging==24.0
    PySocks==1.7.1
    python-dotenv==1.0.1
    requests==2.31.0
    selenium==4.19.0
    sniffio==1.3.1
    sortedcontainers==2.4.0
    trio==0.25.0
    trio-websocket==0.11.1
    typing_extensions==4.11.0
    urllib3==2.2.1
    webdriver-manager==4.0.1
    wsproto==1.2.0

DOCUMENTAÇÃO:
* Selenium:  https://selenium-python.readthedocs.io
* Webdriver Manager: https://pypi.org/project/webdriver-manager/
<hr>

# Transcrever Áudio
Transcreve o áudio de um vídeo ou de arquivo, que esteja na pasta "Transcrever Áudio". Há primeira parte, mostra a transcrição completa no terminal, a segunda salva em um arquivo TXT separando as frases por segundo, e a terceira salva todo o texto completo em arquivo TXT.

Detecta qual automaticamente a linguagem do audio e transcreve em texto para a mesma linguagem

**Opções de Modelo**
* ``tiny``
* ``base``
* ``small``
* ``medium``
* ``large``

Quanto melhor for a opção do modelo, maior será o consumo da GPU.

**Modificando**
* VIDEO_PATH = Adiciona o nome do arquivo que contém o áudio 
* MODEL_NAME = Tipo do modelo que será usado, pode ser alterado com base nas `Opções de Modelo`.