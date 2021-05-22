import shutil
import os


def remove_file(old_path, new_path):
    # print(old_path)
    # print(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    filelist = os.listdir(old_path)  # 列出该目录下的所有文件,listdir返回的是文件列表是不包含路径的。
    # print(filelist)

    cout = 0
    for file in filelist:
        filename, extension = os.path.splitext(file)
        # if extension == ".png" or extension == ".jpg":
        if extension == ".json":
            print(file)
            src = os.path.join(old_path, file)
            dst = os.path.join(new_path, file)
            # print('src:', src)
            # print('dst:', dst)
            shutil.copy(src, dst)
            cout += 1
    print(cout)


if __name__ == '__main__':
    # remove_file("E:\\数据集\\total", "E:\\Desk\\JPEGImages")
    remove_file("H:\\数据集\\total_1000", "H:\\数据集\\first_1000\\JSON")
