import os
import shutil
import inspect


def select_person(annotation, images, output_annotations):
    # 第三步，根据已划分好的训练集和验证集图片路径，从VOC文件结构的Annotation中找到对应的xml文件划分
    if not os.path.exists(output_annotations):
        os.makedirs(output_annotations)
    for jpg_file in os.listdir(images):
        # print(txt_file)
        jpg_name, extension = os.path.splitext(jpg_file)
        # print(txt_name)
        src = os.path.join(annotation, jpg_name + ".xml")
        dst = os.path.join(output_annotations, jpg_name + ".xml")
        shutil.copy(src, dst)
        print("已完成", dst)


if __name__ == '__main__':
    Annotation = "E:\\desk_VOC\\Annotations"

    train_source_images = "E:\\voc_desk\\desk-123-2000\\images\\train"
    train_output_annotation = "E:\\voc_desk\\desk-123-2000\\annotation\\train"
    select_person(Annotation, train_source_images, train_output_annotation)

    valid_source_images = "E:\\voc_desk\\desk-123-2000\\images\\valid"
    valid_output_annotation = "E:\\voc_desk\\desk-123-2000\\annotation\\valid"
    select_person(Annotation, valid_source_images, valid_output_annotation)