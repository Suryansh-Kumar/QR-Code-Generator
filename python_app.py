
# ? Install all the libraries needed
# ? create a functionthat collects text and converts it to a qr code
# ? save the qr code as an image
# ? run the functions

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save("qrcode/qrimg.png")

url = input("Enter your url: ")
generate_qrcode(url)