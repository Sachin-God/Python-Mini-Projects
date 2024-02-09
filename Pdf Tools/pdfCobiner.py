from glob import glob
import pikepdf

newPDF = pikepdf.Pdf.new()

for file in glob("*.pdf"):
    oldPDF = pikepdf.Pdf.open(file)
    newPDF.pages.extend(oldPDF.pages)
newPDF.save("Joined.pdf")