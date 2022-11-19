from PIL import Image
im = Image.open('birdnest.jpg')
print(im.mode)
r, g, b = im.split()
newr = r.point(lambda i: i < 100 and i or 255)  # 选择red通道值低于100的像素点
newg = g.point(lambda i: i < 100 and i or 255)  # 选择green通道值低于100的像素点
newb = b.point(lambda i: i < 100 and i or 255)  # 选择blue通道值低于100的像素点
om = Image.merge(im.mode, (r, newg, newb))
om.save('birdnestMerge-less-100-keep-r.jpg')

om = Image.merge(im.mode, (newr, g, newb))
om.save('birdnestMerge-less-100-keep-g.jpg')

om = Image.merge(im.mode, (newr, newg, b))
om.save('birdnestMerge-less-100-keep-b.jpg')

om = Image.merge(im.mode, (newr, newg, newb))
om.save('birdnestMerge-less-100.jpg')
