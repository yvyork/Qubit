from fpdf import FPDF
import os

# cups library for python!!!

class PDF(FPDF):

    def printTicket(number):
        pdf = PDF('P', 'mm', (62,29))
        pdf.add_page()
        pdf.set_font('Arial', 'B', 40)
        pdf.cell(w=20, h=1, txt='# %d' % number, border=0, ln=1, align='C')
        pdf.output('ticket.pdf', 'F')
        os.popen("lpr -P Qubit -o page-ranges=2 -o media=Custom.62x29mm qubit/ticketpdf/ticket.pdf")

        os.system("sleep 1")

        os.remove('ticket.pdf')
