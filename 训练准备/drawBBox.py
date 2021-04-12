import os
import cv2
import xml.etree.ElementTree as ET


def xmin_ymin(xml_path, image_path, out_path):
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

            for image_file in os.listdir(image_path):

                full_path = os.path.join(image_path, image_file)

                image = cv2.imread(full_path)
                image = cv2.rectangle(image, left, right, (0, 0, 255), 4)
                out_file = os.path.join(out_path, image_file)
                cv2.imshow('demo', image)
                cv2.waitKey(0)


if __name__ == '__main__':
    xml = "E:\\Desk\\voc"
    jpg_path = "E:\\Desk\\JPEGImages"
    outfile = "E:\\Desk\\draw"
    xmin_ymin(xml, jpg_path, outfile)
