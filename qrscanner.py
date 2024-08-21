import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from PIL import pillow

# Create a QR code instance with the given data
my_qr = qrcode.make("https://youtube.com")
#replace desired link at the in the bracket

# Save the QR code as an image file
my_qr.save("myqr.png")

# Optional: Resize the QR code image (e.g., scale by a factor of 9)
img = Image.open("myqr.png")
new_size = (img.width * 9, img.height * 9)
img = img.resize(new_size, Image.NEAREST)
img.save("myqr_scaled.png")
