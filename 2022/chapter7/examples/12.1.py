from PIL import Image
import math
# http://paulbourke.net/dataformats/asciiart/
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
    im = Image.open('astro.jpg')
    WIDTH, HEIGHT = 270, 101
    im = im.resize((WIDTH, HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt", "w")
    fo.write(txt)
    fo.close()


ascii_char.reverse()
main()
#print(len(ascii_char))
