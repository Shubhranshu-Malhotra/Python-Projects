import PyPDF2

# Open the original and the watermark pdf
with open('D:/Projects/Python-Projects/data/pdfs/super.pdf', 'rb') as pdf_file:
    # read content of original file
    page_reader = PyPDF2.PdfFileReader(pdf_file)
    with open('D:/Projects/Python-Projects/data/pdfs/wtr.pdf', 'rb') as watermark_file:
        # read content of the watermarker file
        watermark_reader = PyPDF2.PdfFileReader(watermark_file)

        # Store the watermark from watermark page
        watermark = watermark_reader.getPage(0)

        # initialize a writer object
        writer = PyPDF2.PdfFileWriter()

        # Loop over all the pages in original file
        for num in range(page_reader.numPages):
            # get each page of original file
            page = page_reader.getPage(num)
            # Merge each page with the watermark stored earlier
            page.mergePage(watermark)
            # add each watermarked page to writer object
            writer.addPage(page)

        # Write all watermarked pages to and external file
        with open('./data/pdfs/watermarked_super.pdf', 'wb') as write_pdf:
            writer.write(write_pdf)