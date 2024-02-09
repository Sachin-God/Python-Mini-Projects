import pikepdf
import os

file = input('Enter your File Name: ')  # file name to be exactly precise and to be in same Directory

oldPDF = pikepdf.Pdf.open(file)

for i, page in enumerate(oldPDF.pages):
    newPDF = pikepdf.Pdf.new()
    newPDF.pages.append(page)
    name = "test" + str(i) + ".pdf"
    newPDF.save(name)