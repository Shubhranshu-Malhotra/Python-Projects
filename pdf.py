import PyPDF2

with open('./data/pdfs/dummy.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./data/pdfs/tilted.pdf', 'wb') as write_pdf:
        writer.write(write_pdf)