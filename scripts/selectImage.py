import os
import sys
from PIL import Image


def selectfile(source, out):
    if not os.path.exists(out):
        os.makedirs(out)
    cout = 0
    for file in os.listdir(source):
        filename, extension = os.path.splitext(file)
        if extension == ".png" or extension == ".jpg":
            print(file)
            cout += 1
            # kk = os.path.join(source + "\\" + file)
            img = Image.open(os.path.join(source, file))
            img.save(out + '/a' + file)  # 不加/a会把目录当成名字保存， 不知道为什么

    print(cout)


if __name__ == '__main__':
    sourcefile = "E:\\数据集\\total"
    outfile = "E:\\Desk\\JPEGImages"

    selectfile(sourcefile, outfile)
