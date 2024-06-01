import qrcode

image = qrcode.make("https://mdhasanuzzaman.streamlit.app/")
image.save("qr.png")