"""from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
"""
from pypdf import PdfWriter
import os
merger=PdfWriter()
files=os.listdir("pdfs")
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdfs")
merger.close()