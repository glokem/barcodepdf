from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39


string = '01234567' # This is the 'barcode'. barcode generation only takes strings..?

# co-ordintaes of barcode placement. Co-ordinate anchor seems to scale with barwidth in the barcode generation field
x_var=0
y_var=10

# <create barcode pdf>
packet = StringIO.StringIO()

# barcode generation and text placement here. Loop this section for multipe barcode placements.
slab = canvas.Canvas(packet, pagesize=A4)
slab.setFillColorRGB(0,0,0) # change colours of text here
barcode = code39.Extended39(string,barWidth=.5*mm,barHeight=10*mm, checksum=0) # code39 type barcode generation here
barcode.drawOn(slab, x_var*mm , y_var*mm) # coordinates for barcode?
slab.setFont("Courier", 25) # font type and size0
slab.drawString(40, 10, string) # coordinates for text..?(xpos, ypos, string) unknown units. 1/10th of barcode untins??

slab.save()
# </pdf created>

packet.seek(0)
new_pdf = PdfFileReader(packet)

existing_pdf = PdfFileReader(file("template.pdf", "rb"))
output = PdfFileWriter()

#zero is first page?? Not sure how to do multiple pages...?
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

#write everythinbg to output pdf
outputStream = file("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
