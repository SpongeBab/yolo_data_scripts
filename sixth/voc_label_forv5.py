import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets = [('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
sets = ['train', 'valid']
# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
# "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes = ["studentDesk"]


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


# 为了v5结构准备，直接将这个文件复制到数据集文件夹目录下
# 根据图片名生成图片标签文件，和训练路径，验证路径
def convert_annotation(images_set, image_id):
    in_file = open('E:\\desk_VOC\\annotation\\%s\\%s.xml' % (images_set, image_id))
    out_file = open('E:\\desk_VOC\\labels\\%s\\%s.txt' % (images_set, image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

for image_set in sets:
    if not os.path.exists('E:\\desk_VOC\\labels/%s' % image_set):
        os.makedirs('E:\\desk_VOC\\labels\\%s' % image_set)
    image_ids = open('E:\\desk_VOC\\ImageSets\\Main\\%s.txt' % image_set).read().strip().split()
    print(image_ids)
    list_file = open('%s.txt' % image_set, 'w')
    for image_id in image_ids:
        print(image_id)
        list_file.write('E:\\desk_VOC\\images\\%s\\%s.jpg\n' % (image_set, image_id))
        convert_annotation(image_set, image_id)
    list_file.close()
