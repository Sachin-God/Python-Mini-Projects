import pikepdf
from pikepdf import PdfImage

page = int(input("Enter the page number : ")) - 1
file = input("PDF Name : ")

pdf = pikepdf.Pdf.open(file)
Page = pdf.pages[page]

pageKeys = list(Page.images.keys())

for i,imgd in enumerate(pageKeys):
    pdfimage = PdfImage(Page.images[imgd])
    pdfimage.extract_to(fileprefix="test1")