from PIL import Image
im = Image.open('birdnest.jpg')
print(im.mode)
r, g, b = im.split()
threshhold = 200
newr = r.point(lambda i: i > threshhold and i or 0)  # 选择red通道值大于200的像素点
newg = g.point(lambda i: i > threshhold and i or 0)  # 选择green通道值大于200的像素点
newb = b.point(lambda i: i > threshhold and i or 0)  # 选择blue通道值大于200的像素点
om = Image.merge(im.mode, (r, newg, newb))
om.save('birdnestMerge-greater-{}-keep-r.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, g, newb))
om.save('birdnestMerge-greater-{}-keep-g.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, newg, b))
om.save('birdnestMerge-greater-{}-keep-b.jpg'.format(threshhold))

om = Image.merge(im.mode, (newr, newg, newb))
om.save('birdnestMerge-greater-{}.jpg'.format(threshhold))

