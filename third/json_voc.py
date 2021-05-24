import os
import json

headstr = """\
<annotation>
    <folder>%s</folder>
    <filename>%s</filename>
    <path>%s</path>
    <source>
        <database>desk</database>
    </source>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
"""
objstr = """\
    <object>
        <name>%s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""

tailstr = '''\
</annotation>
'''


def write_xml(anno_path, head, objs, tail):
    f = open(anno_path, "w")
    if not os.path.exists(anno_path):
        os.makedirs(anno_path)
    f.write(head)
    for obj in objs:
        f.write(objstr % (obj[0], obj[1], obj[2], obj[3], obj[4]))

    f.write(tail)


def json_to_xml(json_path, xml_path):
    # global xml_name
    if not os.path.exists(xml_path):
        os.makedirs(xml_path)
    dir = os.listdir(json_path)
    for file in dir:
        with open(os.path.join(json_path, file), encoding="utf-8") as load_f:
            json_dict = json.load(load_f)

        # json数据集格式
        # json_dict = {
        #     "annotations":{},
        #     "door":{},
        #     "images":{},
        #     "studentDesk":{},
        #     "teacherDesk":{},
        #     "window":{},
        # }

        studentDesk = json_dict["studentDesk"]
        teacherDesk = json_dict["teacherDesk"]
        images = json_dict["images"]  # images是一个数组[]

        # headstr

        filename = images[0]  # 数组中的元素是对象 {}

        imagefile_list = os.path.split(filename["file_name"])

        jpg_name = imagefile_list[1]

        file, extension = os.path.splitext(jpg_name)
        if extension == ".jpg":
            xml_name = jpg_name.replace(".jpg", ".xml")
            filename["file_name"] = os.path.join(xml_path, xml_name)

        depth = 3
        width = images[1]
        height = images[3]

        head = headstr % (xml_path, jpg_name, os.path.join(xml_path, jpg_name), width, height, depth)
        # print(head)

        # objstr
        dataset = []

        for segmentation in studentDesk:
            coordinate = segmentation["segmentation"]
            coordinate = coordinate[0]

            x = []
            y = []
            x = coordinate[::2]
            xmin = min(x)
            xmax = max(x)
            y = coordinate[1::2]
            ymin = min(y)
            ymax = max(y)

            name = "studentDesk"

            dataset.append([name, xmin, ymin, xmax, ymax])
        tail = tailstr

        write_xml(os.path.join(xml_path, xml_name), head, dataset, tail)


if __name__ == '__main__':
    json_path = "E:\\voc_desk\\desk_3_400\\json"  # 该目录为存放json文件的路径
    xml_path = "E:\\voc_desk\\desk_3_400\\annotations"  # 该目录为放xml文件的路径
    json_to_xml(json_path, xml_path)
