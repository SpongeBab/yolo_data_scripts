import os


# 根据训练集和验证集图片生成图片id
def generate_txt(source_path, txt_path):
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)

    file_list = os.listdir(source_path)
    temp = os.path.basename(source_path)
    txt = os.path.join(txt_path, temp+'.txt')
    txt_file = open(txt, "w")
    count = 0
    for file_obj in file_list:
        count += 1
        file_path = os.path.join(source_path, file_obj)
        file_name, file_extend = os.path.splitext(file_obj)
        txt_file.write(file_name + "\n")
    txt_file.close()
    print(count)


if __name__ == '__main__':
    source_train_folder = 'E:\\Dataset\\coco-2\\images\\train'
    train_txt_output = 'E:\\Dataset\\desk-4\\ImageSet\\Main'
    generate_txt(source_train_folder, train_txt_output)

    source_valid_folder = 'E:\\Dataset\\desk-4\\images\\valid'
    valid_txt_output = 'E:\\Dataset\\desk-4\\ImageSet\\Main'
    generate_txt(source_valid_folder, valid_txt_output)

