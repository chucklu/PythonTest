from PIL import Image
im = Image.open('birdnest.jpg')
print(im.mode)
r, g, b = im.split()
newr = r.point(lambda i: 0)  # 移除红色通道
om = Image.merge(im.mode, (newr, g, b))
om.save('birdnestRemoveRed.jpg')
