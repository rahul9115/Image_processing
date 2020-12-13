from PIL import Image
img=Image.open("1.png")
img=img.resize((28,28))

print(img.size)
