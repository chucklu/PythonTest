from PIL import Image
im = Image.open('cat.jpg')
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('catBGR.jpg')

om = Image.merge("RGB", (b, r, g))
om.save('catBRG.jpg')

om = Image.merge("RGB", (g, b, r))
om.save('catGBR.jpg')

om = Image.merge("RGB", (g, r, b))
om.save('catGRB.jpg')

om = Image.merge("RGB", (r, b, g))
om.save('catRBG.jpg')