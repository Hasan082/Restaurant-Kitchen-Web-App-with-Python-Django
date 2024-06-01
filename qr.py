import qrcode

image = qrcode.make("https:127.0.0.1:8080")
image.save("qr.png")