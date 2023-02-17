import qrcode as qr

# img = qr.make('argument')

data = input('  Enter:\n')

img = qr.make(data)
# type(img)
img.save('data.png')
