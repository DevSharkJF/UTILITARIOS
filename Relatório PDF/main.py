import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 

tabela = pd.read_csv("manutencao.csv")

for linha in tabela.index:
    nome = tabela.loc[linha, "Nome do Cliente"]
    maquina = tabela.loc[linha, "Tipo de Máquina"]
    defeito = tabela.loc[linha, "Defeito"]
    valor = tabela.loc[linha, "Valor da Manutenção"]
    servico = tabela.loc[linha, "Serviço Executado"]

    documento_pdf = canvas.Canvas(f"relatório de Horas {nome}.pdf", A4)

    documento_pdf.setFont("Helvetica-Bold", 18)
    documento_pdf.drawString(100, 750, "Relatório de Manutenção de Computadores")

    documento_pdf.setFont("Helvetica", 12)
    distancia = 30

    documento_pdf.drawString(100, 700, f"Nome do Cliente: {nome}")
    documento_pdf.drawString(100, 700 - 1 * distancia, f"Tipo de Máquina: {maquina}")
    documento_pdf.drawString(100, 700 - 2 * distancia, f"Defeito: {defeito}")
    documento_pdf.drawString(100, 700 - 3 * distancia, f"Valor: {valor}")
    documento_pdf.drawString(100, 700 - 4 * distancia, f"Serviço: {servico}")
    documento_pdf.drawString(100, 650 - 5 * distancia, "Relatório Gerado com Python: Pandas e Reportlab")
    documento_pdf.drawString(100, 650 - 6 * distancia, "Todos os dados foram gerados pelo ChatGPT")

    documento_pdf.save()