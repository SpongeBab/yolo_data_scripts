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
        print("obj:", obj)

        f.write(objstr % (obj[0], obj[1], obj[2], obj[3], obj[4]))

    f.write(tail)


def json_to_xml(json_path, xml_path):
    if not os.path.exists(xml_path):
        os.makedirs(xml_path)
    dir = os.listdir(json_path)
    print("json_path:", json_path)
    print("文件列表:", dir)
    for file in dir:
        print("当前文件：", file)
        file_list = file.split(".")
        # print("文件名：", file_list[0])
        # print("文件后缀：", file_list[1])
        with open(os.path.join(json_path, file), encoding="utf-8") as load_f:
            # print("json路径：", load_f)
            json_dict = json.load(load_f)
        print('json_dict:', json_dict)

        # for i, listname in enumerate(json_dict):
        #     print(i)
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
        # print('images:', images)

        # headstr
        # filename = studentDesk["name"]
        filename = images[0]  # 数组中的元素是对象 {}
        # print("file_name:", filename)
        imagefile_list = os.path.split(filename["file_name"])
        # print("imagefile_list:", imagefile_list)
        jpg_name = imagefile_list[1]
        # print("jpg_name:", jpg_name)
        file, extension = os.path.splitext(jpg_name)

        xml_name = ""
        if extension == ".jpg":
            xml_name = jpg_name.replace(".jpg", ".xml")
            # print("xml_name:", xml_name)

            filename["file_name"] = os.path.join(xml_path, xml_name)
        # print(filename)

        depth = 3

        # width = studentDesk["size"]["width"]
        # height = studentDesk["size"]["height"]
        width = 1920
        height = 1080

        head = headstr % (xml_path, jpg_name, os.path.join(xml_path, jpg_name), width, height, depth)
        # print(head)

        # objstr
        dataset = []

        for segmentation in studentDesk:
            # print(segmentation)
            # print(type(segmentation))  # dict
            # print(segmentation["segmentation"])
            coordinate = segmentation["segmentation"]
            # print(coordinate[0])
            # print(coordinate[0][0])
            # print(type(coordinate))
            coordinate = coordinate[0]
            x = []
            y = []

            x = coordinate[::2]
            print("x:", x)
            # print(type(x))
            xmin = min(x)
            xmax = max(x)
            print(xmin, xmax)
            y = coordinate[1::2]
            print("y:", y)
            ymin = min(y)
            ymax = max(y)

            name = "studentDesk"
            print(name)

            dataset.append([name, xmin, ymin, xmax, ymax])
            print(dataset)
        tail = tailstr

        write_xml(os.path.join(xml_path, xml_name), head, dataset, tail)


if __name__ == '__main__':
    json_path = "E:\\Desk\\Annotation"  # 该目录为存放json文件的路径
    xml_path = "E:\\Desk\\voc"  # 该目录为放xml文件的路径
    json_to_xml(json_path, xml_path)
