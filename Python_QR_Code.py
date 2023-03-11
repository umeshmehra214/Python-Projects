# There are two ways to Generat QR Code in Python ------>

# 1. Simple QR Code
# 2. Advanced QR Code

# First we intall QR module in our system by use this command ----- >   pip install qrcode

# 1. Generating a Simple QR Code :-----

import qrcode
img = qrcode.make("https://www.linkedin.com/in/umeshmehra214/")  
img.save("Linkedin_profile.png")       # A Linkedin_profile QR code image will be created scan QR Code Image and get results  


# 2. Generating an Advanced QR Code : ------

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data('https://github.com/umeshmehra214')
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue")
img.save("Github_profile.png")        # A Github_profile QR code image will be created scan QR Code Image and get results
