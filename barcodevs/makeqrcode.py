
# Importing library
import qrcode
 
# Data to encode
data = {
    "name": "vinod",
    "city": "jaipur",
    "phone No": 3333333333333332
}
a = ['vinod', 'jaipur', 234848]
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 8)
 
# Adding data to the instance 'qr'
qr.add_data(a)
print(type(data))
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'orange',
                    back_color = 'white')
 
img.save('MyQRCode2.png')