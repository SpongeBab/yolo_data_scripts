import os
import cv2
import xml.etree.ElementTree as ET


def xmin_ymin(xml_path):
    left = ()
    right = ()
    for xml_file in os.listdir(xml_path):

        in_file = open(os.path.join(xml_path, xml_file))
        b = []
        tree = ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
            # Element.find() 找带有特定标签的 第一个 子级，然后可以用 Element.text 访问元素的文本内容。
            Bbox = obj.find('bndbox')
            xmin = int(Bbox.find("xmin").text)
            xmax = int(Bbox.find('xmax').text)
            ymin = int(Bbox.find('ymin').text)
            ymax = int(Bbox.find('ymax').text)

            left = (xmin, ymin)
            right = (xmax, ymax)
            print(xml_file)
            print(left, right)


# only can draw one picture
def draw():
    image = cv2.imread('E:\\VOC\\face\\images\\train\\0028_80701002007_20191020135000_5.jpg')
    # image = cv2.resize(image, (640, 360))
    print(image.shape)
    tree = ET.parse('E:\\VOC\\face\\annotation\\train\\0028_80701002007_20191020135000_5.xml')
    root = tree.getroot()
    for obj in root.iter('object'):
        # Element.find() 找带有特定标签的 第一个 子级，然后可以用 Element.text 访问元素的文本内容。
        Bbox = obj.find('bndbox')
        xmin = int(float(Bbox.find("xmin").text))
        xmax = int(float(Bbox.find('xmax').text))
        ymin = int(float(Bbox.find('ymin').text))
        ymax = int(float(Bbox.find('ymax').text))

        left = (xmin, ymin)
        right = (xmax, ymax)
        print(left, right)
        image = cv2.rectangle(image, left, right, (0, 0, 255), 3)
        cv2.imshow("1", image)
        cv2.waitKey(0)

    cv2.imwrite("result.jpg", image)


if __name__ == '__main__':
    draw()
