import shutil
import os
from sklearn import model_selection
import numpy as np

def split_file(All_path, train_path, valid_path):
    # 第二步，将图片划分为训练集和验证集
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(valid_path):
        os.makedirs(valid_path)
    filelist = os.listdir(All_path)  # 列出该目录下的所有文件,listdir返回的是文件列表是不包含路径的。
    # print(filelist)
    # open(train_path, 'a+')
    # open(valid_path, 'a+')
    count = 0
    for file in filelist:
        filename, extension = os.path.splitext(file)
        src = os.path.join(All_path, file)
        train_jpg = os.path.join(train_path, file)
        valid_jpg = os.path.join(valid_path, file)
        # print('src:', src)
        # print('dst:', dst)
        x = np.array(filelist)
        print(x)
        train, test = model_selection.train_test_split(x, test_size=0.8)
        if count < 4300:
            shutil.copyfile(src, train)
        else:
            shutil.copy(src, test)
        count += 1
        print(count)
    print(count)


if __name__ == '__main__':
    # remove_file("E:\\数据集\\total", "train_path", "valid_path")
    split_file("E:\\qxdetection\\data\\images",
               "E:\\qxdetection\\images\\train",
               "E:\\qxdetection\\images\\valid")
