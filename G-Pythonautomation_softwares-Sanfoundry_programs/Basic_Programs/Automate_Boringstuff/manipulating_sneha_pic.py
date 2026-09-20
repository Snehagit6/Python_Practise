from PIL import Image
img = Image.open("F:\\Sneha_J2Pics\\Photo.png")
img = img.rotate(180)
img.show()
print(img.mode)