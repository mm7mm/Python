from PIL import Image
myImage =Image.open("G:\Corses\Python\Python\m.jpg")
m=myImage.convert("L")
m.show()