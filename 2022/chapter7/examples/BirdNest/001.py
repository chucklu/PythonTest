from PIL import Image
im = Image.open("birdnest.jpg")
im.save("birdnet.png")

im.thumbnail((128,128))
im.save("birdnesetTN.jpg","JPEG")