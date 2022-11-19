from PIL import Image
im = Image.open('birdnest.jpg')
print(im.mode)
r, g, b = im.split()
newr = r.point(lambda i: 0)  # 将green通道颜色值变为原来的0.9倍
om = Image.merge(im.mode, (newr, g, b))
om.save('birdnestRemoveRed.jpg')
