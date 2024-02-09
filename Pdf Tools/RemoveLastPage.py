import pikepdf
import os

file = input('Enter your File Name: ')  # file name to be exactly precise and to be in same Directory

with pikepdf.open(file) as pdf:
    pdfPages = len(pdf.pages)
    del pdf.pages[-1]
    pdf.save('output.pdf')