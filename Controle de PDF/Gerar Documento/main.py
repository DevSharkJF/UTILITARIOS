# CRIADOR DE PDF
from fpdf import FPDF
import os

funcionario = "Mano Deyvin"
cpf = "123.456.789-00"
salario = "20.000,00"
empresa = "Mega Brain"
cnpj = "12.345.678/0001-00"

texto_recibo = f"Pelo presente documento, eu {funcionario}, portador do CPF {cpf}, declado que recebi o valor de R$ {salario} referente ao meu trabalho na empresa {empresa}, inscrita sob o CNPJ {cnpj}."

pdf = FPDF()
pdf.add_page()
pdf.ln(15)
pdf.set_font("helvetica", "", 15)
pdf.multi_cell(txt = texto_recibo, w = 0, align = "c")
pdf.ln(15)

pdf.set_font("helvetica", "", 12)
pdf.cell(txt="Sendo assim, firmo o presente recibo para que produza seus efeitos legais.", w = 0, align = "c")
pdf.ln(30)

pdf.set_font("helvetica", "", 14)
pdf.cell(txt = "___________________________, ___ de _________ de _____", w = 0, align = "c")
pdf.ln(30)

pdf.cell(txt = "_________________________________________", w = 0, align = "c")
pdf.ln(10)

pdf.set_font("helvetica", "", 15)
pdf.cell(txt = funcionario, w = 0, align = "c")

output_path = os.path.join(os.path.dirname(__file__), "recibo.pdf")
pdf.output(output_path)