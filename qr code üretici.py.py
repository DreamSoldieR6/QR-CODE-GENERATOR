import pyqrcode # Imported pyqrcode Module

data = "https://github.com/CodingShack/QR-Code-Generator-in-Python/blob/main/README.md" # Declaring the Variables

image = pyqrcode.create(data) # Creating a Function

image.png("image_qrcode.png",scale=8) # Saving the Image