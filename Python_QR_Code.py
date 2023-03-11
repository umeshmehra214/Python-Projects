# first we intall the qrcode in our terminal ---- pip install qrcode

# 1 way to create simple QR Code--->

# import qrcode

# img = qrcode.make("https://www.linkedin.com/in/umeshmehra214/")  
# img.save("text.png")

# 2 Way to create QR Code----->

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data('https://www.sololearn.com/profile/28491225')
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue")
img.save("newqrcode.png")