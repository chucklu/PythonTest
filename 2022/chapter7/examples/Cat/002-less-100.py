from PIL import Image
im = Image.open('cat.jpg')
print(im.mode)
r, g, b = im.split()
threshhold = 100
newr = r.point(lambda i: i < threshhold and i or 255)  # 选择red通道值低于100的像素点
newg = g.point(lambda i: i < threshhold and i or 255)  # 选择green通道值低于100的像素点
newb = b.point(lambda i: i < threshhold and i or 255)  # 选择blue通道值低于100的像素点
om = Image.merge(im.mode, (r, newg, newb))
om.save('birdnestMerge-less-{}-keep-r.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, g, newb))
om.save('birdnestMerge-less-{}-keep-g.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, newg, b))
om.save('birdnestMerge-less-{}-keep-b.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, newg, newb))
om.save('birdnestMerge-less-{}.jpg'.format(threshhold))
