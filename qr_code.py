import qrcode as qr
img = qr.make("https://www.w3schools.com/")
img.save("LearnCode.png")