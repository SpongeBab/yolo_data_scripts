import os


def convert2txt(source, output):
    # open(output, "w")
    files = os.listdir(source)
    # print(files) # ['1.jpeg', '2.jpeg']
    for file in files:
        # print(file)   # 1.jpeg
        filename, extension = os.path.splitext(file)
        print(filename)  # 1
        # print(extension)  # .jpg
        fullname = os.path.join(source, file)
        print(file)
        # print(fullname)

        output.write(filename + "\n")


if __name__ == '__main__':
    sourcefile = "E:\\图像目标检测\\YOLO代码\\darknet-master\\build\\darknet\\x64\\data\\voc\\VOC\\VOC2012\\JPEGImages"
    out = open("E:\\图像目标检测\\YOLO代码\\darknet-master\\build\\darknet\\x64\\data\\voc\\VOC\\VOC2012\\ImageSets"
               "\\Main\\train.txt", "w")
    convert2txt(sourcefile, out)
