import pikepdf

file = input("Enter Your File Name : ")

pdf = pikepdf.Pdf.open(file)
pdf.pages.reverse()
pdf.save(file + "_Reversed.pdf")