# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:28:05 2020

@author: ngqua
"""

import numpy as np
a= np.array([[1,3,4],[2,4,4],[2,3,4]])
b= np.array([[3,3,3],[2,1,4],[1,1,1]])
print("matix a")
print(a)
print("matix b")
print(b)
print("---------2222---------")
print("Tong :")
print(a+2)
print("Hieu :")
print(a-2)
print("Tich :")
print(a*2)
print("Thuong :")
print(a/2)
print("---------------------")
print("Tong :")
print(a+b)
print("Hieu :")
print(a-b)
print("Tich :")
print(a.dot(b))
print("Thuong :")
print(a.dot(np.fliplr(b)))