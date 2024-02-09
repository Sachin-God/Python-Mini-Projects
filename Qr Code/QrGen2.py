import qrcode
from PIL import Image

url = input("Enter your url: ")
fill = input("Enter your fill Color: ")
back = input("Enter your Backgroung color: ")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color=fill,back_color=back)
img.save("Qr.png")