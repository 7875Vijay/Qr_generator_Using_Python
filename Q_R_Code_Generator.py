# first we need to install qrcode using cmd[pip install qrcode]
# and alse install image using cmd[pip install image]

import qrcode
import image

qr = qrcode.QRCode(
    version = 15,  #15 means the version of the qr code high the number bigger the code image and coplicated picture.
    box_size = 10,  # size of the box where qr code will be displayed
    border = 5  #it is the white part of the image -- border in all 4 sides with white color
)

data = "https://www.instagram.com/vijaypatil5270/?hl=en"
# as i have given the path of my instagram account that the qr will generate the code for this link
# otherwise we can give any other data in the double cote of the data
qr.add_data(data)
qr.make(fit = True)
img = gr.make_image(fill = "black", back_color = "white")
img.save("test.png")
