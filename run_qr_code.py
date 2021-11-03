import qrcode

img = qrcode.make('https://www.jcchouinard.com/python-for-seo/')
img.save('output/my_qr_code.png')