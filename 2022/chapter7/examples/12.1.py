from PIL import Image
import math
# http://paulbourke.net/dataformats/asciiart/
# 灰色值指黑白图像中的颜色深度，白色为255，黑色为0。
# 白色的rgb是(255,255,255)，灰度值是255
ascii_char = list(
    '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,"^`\'.')


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    percent = (gray+1)/256.0  # 灰度值在256中所占的百分比
    index = math.floor(len(ascii_char)*percent)  # 计算出index
    return ascii_char[index]  # 对应灰度值与字符

    # unit = 256 / len(ascii_char)
    # return ascii_char[int(gray//unit)]


def main():
    im = Image.open('doraemon.jpg')
    WIDTH, HEIGHT = 103, 123
    im = im.resize((WIDTH, HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("doraemon.txt", "w")
    fo.write(txt)
    fo.close()


# ascii_char.reverse() #黑色背景启用这个,
main()
# print(len(ascii_char))
