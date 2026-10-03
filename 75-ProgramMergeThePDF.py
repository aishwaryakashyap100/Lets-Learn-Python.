# Exercise 8-

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

folder = "75.tutorial"

files = [
    os.path.join(folder, file)
    for file in os.listdir(folder)
    if file.lower().endswith(".pdf")
]

print(files)

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print("PDFs merged successfully!")