# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

from numpy import *
# 20180711
# ~
# 2018...
class optStruct:
    def __init__(self,dataMatIn,classLabels,C,toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]