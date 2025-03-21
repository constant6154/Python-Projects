import qrcode
import os

data = 'Porashuna bhalo lagena'
save_path = 'E:\QR\myqr.png'

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save(save_path)

# Show the QR code
img.show()
