# -*- coding: utf-8 -*-
import operator
import numpy as np

def create_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataset, labels, k):
    diff_mat = np.tile(inX, (dataset.shape[0], 1)) - dataset
    sq_dist = (diff_mat ** 2).sum(axis=1)
    dist = sq_dist ** 0.5 # 求得数据集中的点与当前点的距离
    sorted_dist_indicies = dist.argsort() # 按数值从小到大排序的索引值
    class_count = {}
    # 选择距离最小的 k 个点
    for i in range(k):
        lb = labels[sorted_dist_indicies[i]]
        class_count[lb] = class_count.get(lb, 0) + 1

    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]

if __name__ == '__main__':
    group, labels = create_dataset()
    print classify0([0, 0], group, labels, 3)
