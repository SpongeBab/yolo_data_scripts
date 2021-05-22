import os
from os import listdir, getcwd
from os.path import join

if __name__ == '__main__':
    source_folder = '../VOC/VOC2012/JPEGImages'
    train = '../VOC/VOC2012/ImageSets/Main/train.txt'
    test = '../VOC/VOC2012/ImageSets/Main/test.txt'
    file_list = os.listdir(source_folder)
    train_file = open(train, 'a')
    test_file = open(test, 'a')
    count = 0
    for file_obj in file_list:
        count += 1
        file_path = os.path.join(source_folder, file_obj)

        file_name, file_extend = os.path.splitext(file_obj)

        # file_num = int(file_name)

        if count <= 800:
            train_file.write(file_name + '\n')
        else:
            test_file.write(file_name + '\n')
    train_file.close()
    test_file.close()
