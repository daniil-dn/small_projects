
import qrcode
# from pyzbar.pyzbar import decode
from PIL import Image
import cv2 as cv

data = 'Don\'t forget to drink some water'

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')
img.save("./qr.jpeg")


result = cv.imread("./qr.jpeg")
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(result)
print(retval)