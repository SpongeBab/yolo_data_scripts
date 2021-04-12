import inspect
import os
import random
import sys


def extract_log(log_file, new_log_file, key_word):
    with open(log_file, 'r') as f:
        fb = f.readlines()
        with open(new_log_file, 'w') as train_log:
            # f = open(log_file)
            # train_log = open(new_log_file, 'w')
            for line in fb[6000:]:
                # 去除多gpu的同步log
                if 'Syncing' in line:
                    continue
                # 去除除零错误的log
                if 'nan' in line:
                    continue
                if key_word in line:
                    train_log.write(line)
    f.close()
    train_log.close()


extract_log('F:/darknet-master/yolov4_train.log', 'train_log_loss.txt', 'rate')
