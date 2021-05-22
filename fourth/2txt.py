import os

# 根据图片名生成供label生成txt标签的train和valid文件
if __name__ == '__main__':
    source_folder = './JPEGImages'
    path = './ImageSets/Main'
    file_list = os.listdir(source_folder)
    if not os.path.exists(path):
        os.makedirs(path)
    train_txt = os.path.join(path, "train.txt")
    test_txt = os.path.join(path, "valid.txt")
    train_file = open(train_txt, 'a')
    test_file = open(test_txt, 'a')
    count = 0
    for file_obj in file_list:
        count += 1
        file_path = os.path.join(source_folder, file_obj)
        file_name, file_extend = os.path.splitext(file_obj)

        if count <= 1800:
            train_file.write(file_name + '\n')
        else:
            test_file.write(file_name + '\n')
    print(count)
    train_file.close()
    test_file.close()
