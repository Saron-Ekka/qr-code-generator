import qrcode
import image

qr = qrcode.QRCode(
    version = 15, #15 means version of qr code , high the no. bigger the code image and complicated pictures
    error_correction= qrcode.constants.ERROR_CORRECT_H ,
    box_size=10, #size of the box where qr code will be displayed
    border= 4 #it is the white part of image--border in all 4 sides with white colour
)

data = "https://www.instagram.com/ietebits/"

qr.add_data(data);
qr.make(fit = True);
img = qr.make_image(fill_color="Blue", back_color = "white");
img.save("test.png");