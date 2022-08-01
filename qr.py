import qrcode
from PIL import Image
boxSize = 10
border = 5
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   boxSize, border)
url = 'https://github.com/Uzair-Imtiaz'
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color="grey", back_color="black")
img.save('qr.png')
