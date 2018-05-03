# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
#20180502

# "SVM是最好的现成的分类器。"——这里说的“现成”指的是分类器不加修改即可直接使用。同时，这就意味着在数据上应用基本形式的SVM分类器就可以得到低错误率的结果。
# SVM能够对训练集之外的数据点做出很好的分类决策。

# SVM有很多实现，但本章只关注其中最流行的一种实现，即序列最小优化（Sequential Minimal Optimization，SMO）算法
# 在此之后，将介绍如何使用一种称为核函数（kernel）的方式将SVM扩展到更多数据集上。
# 最后会回顾第1章中手写识别的例子，并考察其能否通过SVM来提高识别的效果。

# （一）基于最大间隔分隔数据
#  优点：泛化错误率低，计算开销不大，结果易解释。
#  缺点：对参数调节和核函数的选择敏感，原始分类器不加修改仅适用于处理二分类问题。
#  适用数据类型：数值型和标称型数据。


#将数据集分隔开来的直线称为分隔超平面（separating hyperplane）。
#所有数据点都在二维平面上，分隔超平面为：一条直线；
#所给数据集是三维的，分隔超平面为：一个平面；
#若数据集是1024维的，分隔超平面为：一个1023维的某某对象。该对象被称为超平面（hyperplane），也就是分类的决策边界。

#希望能采用这种方式来构建分类器：如果数据点离决策边界越远，那么其最后的预测结果也就越可信。
#支持向量（support vector）就是离分隔超平面最近的那些点。
#接下来 要试着最大化支持向量到分隔面的距离，需要找到此问题的优化求解方法。

# （二）寻找最大间隔
# 分隔超平面的形式可以写成：w^Tx+b，向量w和常数b一起描述了所给数据的分隔线或超平面。
# 点A到分隔超平面的距离为：|w^TA+b| / ||w||，这里的常数b类似于Logistic回归中的截距w_0


#P48
#

