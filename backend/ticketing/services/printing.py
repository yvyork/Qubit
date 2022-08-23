from fpdf import FPDF
from pdf2image import convert_from_path
import os


class PDF(FPDF):

    def printTicket(number):
        pdf = PDF('P', 'mm', (62,29))
        pdf.add_page()
        pdf.set_font('Arial', 'B', 40)
        pdf.set_left_margin(20)
        pdf.cell(w=20, h=10, txt='# %d' % number, border=0, ln=0, align='C')
        pdf.output('./ticketpdf/ticket.pdf', 'F')

        images = convert_from_path('./ticketpdf/ticket.pdf', 62)

        for image in images:
            image.save('out.png', 'PNG')

        os.popen ("brother_ql print -l 62 ./ticketpdf/out.png")


