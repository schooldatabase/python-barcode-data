
# Importing library
import qrcode
 
# Data to be encoded
data = 'trilok saini 12323'
py = 12323423
 
# Encoding data using make() function
img = qrcode.make(py)
 
# Saving as an image file
img.save('MyQRCode1.jpg')