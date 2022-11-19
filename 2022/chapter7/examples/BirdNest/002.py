from PIL import Image
im = Image.open('birdnest.jpg')
print(im.mode)
r, g, b = im.split()
newg = g.point(lambda i: i*0.9)  # 将green通道颜色值变为原来的0.9倍
newb = b.point(lambda i: i < 100)  # 选择blue通道值低于100的像素点
om = Image.merge(im.mode, (r, newg, newb))
om.save('birdnestMerge.jpg')
