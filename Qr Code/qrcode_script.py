import qrcode

txt_qrcode = "https://github.com/DevSharkJF"

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)

qr.add_data(txt_qrcode)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="blue")
img.save("qrcode.png")