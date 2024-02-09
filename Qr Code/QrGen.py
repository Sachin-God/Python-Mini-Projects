import qrcode as qr

url = input("Enter your url: ")
img = qr.make(url)
img.save("qr.png")