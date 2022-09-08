from fpdf import FPDF
import os
pdf = FPDF(orientation = 'L', format='A4')
pdf.set_font("courier", size = 10)

s = open('datcom.out').read()
pages = s.split('AUTOMATED STABILITY AND CONTROL METHODS PER APRIL 1976 VERSION OF DATCOM')
#pages = pages[1:]
for i, page in enumerate(pages):
    pdf.add_page()
    pdf.cell(400, 4, txt = "Page "+str(i),
         ln = 1, align = 'L')
    pdf.multi_cell(400, 4, txt = page,
         align = 'L')
 
pdf.output("datcom.out.pdf")  
os.system('open datcom.out.pdf')
