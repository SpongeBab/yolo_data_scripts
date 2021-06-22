import torch
from torch.utils.data import random_split
import shutil
import os
from sklearn import model_selection
import numpy as np


def split_file(data_path, train_path, valid_path):
    # 第二步，将图片划分为训练集和验证集
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(valid_path):
        os.makedirs(valid_path)
    filelist = os.listdir(data_path)  # 列出该目录下的所有文件,listdir返回的是文件列表是不包含路径的。
    # print(filelist)
    # open(train_path, 'a+')
    # open(valid_path, 'a+')
    count = 0
    dataset = os.listdir("E:\\qxdetection\\data\\images")

    train_dataset, test_dataset = random_split(
        dataset=dataset,
        lengths=[4310, 333], # 两者和必须和数据集数量严格相等
        generator=torch.Generator().manual_seed(0)
    )

    print(len(train_dataset))
    print("\n")
    print(list(test_dataset))
    for i in range(len(train_dataset)):
        print(i)
        # print(file)
        # filename, extension = os.path.splitext(file)
        # src = os.path.join(data_path, file)
        train_jpg = os.path.join(data_path, train_dataset[i])
        print(f"train_jpg {train_jpg}")
        shutil.copy(train_jpg, train_path)
    for j in range(len(test_dataset)):
        valid_jpg = os.path.join(data_path, test_dataset[j])
        print(j)
        print(f"valid_jpg {valid_jpg}")
        shutil.copy(valid_jpg, valid_path)




if __name__ == '__main__':
    # remove_file("E:\\数据集\\total", "train_path", "valid_path")
    split_file("E:\\qxdetection\\data\\images",
               "E:\\qxdetection\\images\\train",
               "E:\\qxdetection\\images\\valid")
