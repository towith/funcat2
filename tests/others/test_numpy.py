
# -*- coding: utf-8 -*-
import unittest
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint as print


class TestFuncat2TestCase(unittest.TestCase):

    def test_rank(self):

        my_array = np.array([[1, 56, 55, 15],
                             [5, 4, 33, 53],
                             [3, 6, 7, 19]])

        sorted_array = np.argsort(my_array, axis=0)
        print(f"These are ranks of array values: axis=0 \n {sorted_array}")

    def test_rank2(self):

        my_array = np.array([[1, 56, 55, 15],
                             [5, 4, 33, 53],
                             [3, 6, 7, 19]])

        sorted_array = np.argsort(my_array, axis=1)
        print(f"These are ranks of array values: axis=1 \n {sorted_array}")

    def test_transpose(self):
      t=np.arange(4)  #  插入值0-3
      print(f"原始：{t}")
      print(f"转置对于一维数组而言，numpy.transpose()是不起作用的：{ t.transpose()}")
      
    def test_transpose2(self):
      t=np.arange(16).reshape(4,4)   # 插入0-15，形状为4*4
      print(f"原始：{t}")
      print(f"对于二维数组,数组两个轴axis为（x，y），对应的下标为（0,1），np.transpose()传入的参数为（1,0），即将原数组的0,1轴互换。综上，对二维数组的transpose操作就是对原数组的转置操作。：{ t.transpose()}")
    
    def test_transpose3(self):
      """二维以上的维数组进行transpose的话，不传参则默认将维度反序
      即将原数组的各个axis进行reverse一下，three原始axis排列为（0,1,2），那numpy.transpose()默认的参数为（2，1，0）得到转置后的数组的视图，不影响原数组的内容以及大小。
      我们一步一步来分析这个过程：axis（0，1，2）———>axis(2，1，0) ，transpose后的数组相对于原数组来说，相当于交换了原数组的0轴和2轴。ndarray.shape (2,3,3) ->(3,3,2)
      (2, 1, 0) 分别代表 维度d,  行l, 列c

      #对原始three数组的位置索引下标写出来，如下：
      A=[
             [ [ (0,0,0) , (0,0,1) , (0,0,2)],
             [ (0,1,0) , (0,1,1) , (0,1,2)],
             [ (0,2,0) , (0,2,1) , (0,2,2)]],

             [[ (1,0,0) , (1,0,1) , (1,0,2)],
              [ (1,1,0) , (1,1,1) , (1,1,2)],
              [ (1,2,0) , (1,2,1) , (1,2,2)]]
        ]

      #接着把上述每个三元组的第一个数和第三个数进行交换，得到以下的数组

      B=[[[ (0,0,0) , (1,0,0) , (2,0,0)],
        [ (0,1,0) , (1,1,0) , (2,1,0)],
        [ (0,2,0) , (1,2,0) , (2,2,0)]],

        [[ (0,0,1) , (1,0,1) , (2,0,1)],
        [ (0,1,1) , (1,1,1) , (2,1,1)],
        [ (0,2,1) , (1,2,1) , (2,2,1)]]]

      #最后在原数组中把B对应的下标的元素，写到相应的位置，如（0，2，1）代表放置到d = 0，行 = 2，列 = 1
      #对比看一下，这是原数组
      [[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

        [[ 9, 10, 11],
         [12, 13, 14],
         [15, 16, 17]]]
      # 按照B的映射关系得到最终的数组。
      C=[[[ 0,  9],
        [ 3,  12],
        [ 6,  15]],

        [[ 1, 10],
         [4, 13],
         [7, 16]]

         [[ 2, 11],
         [5, 14],
         [8, 17]]
      ]
      # 最终的结果也就是数组C

      再看自己定义的转置格式：
      arr = np.arange(24).reshape(3, 4, 2)
      print(arr)
      tran_arr = np.transpose(arr, (1, 0, 2)) # axis索引（0，1，2）变为（1，0，2） 
      print(tran_arr)
       

      因为索引号由（0,1,2）变成了（1,0,2），axis第一个和第二个交换，shape 由(3,4,2)变成了(4,3,2)，可知结果矩阵为d = 4，行3，列2。等效于

      arr = np.arange(24).reshape(3, 4, 2)
      np.swapaxes(arr,0,1) #交换axis 0，1
       
      再展开矩阵的位置下标，每个元素交换第一个和第二个，得到最终的位置下标。

      输出结果：

      [[[ 0  1]
        [ 2  3]
        [ 4  5]
        [ 6  7]]

       [[ 8  9]
        [10 11]
        [12 13]
        [14 15]]

       [[16 17]
        [18 19]
        [20 21]
        [22 23]]]

      [[[ 0  1]
        [ 8  9]
        [16 17]]
       
       [[ 2  3]
        [10 11]
        [18 19]]
       
       [[ 4  5]
        [12 13]
        [20 21]] 
       
       [[ 6 7 ]
        [14 15]
        [22 23]]]
      一般用reshape()进行维度转换比较多，直接传入新的维度就行，而不是用下标代替   
      arr = arr.reshape(4,3,2)
       但是实际上二者是有很大区别的，transpose()会将数组进行转置，而reshape()则是按照数组原有的排布顺序，重新按照新维度生成一个依然有序的数组，从以上两图也能看出来
      """
      t=np.arange(18).reshape(2,3,3)
      print(f"原始：{t}")
      print("二维以上的维数组进行transpose的话，不传参则默认将维度反序;")
      print(f"对于三维数组,数组两个轴axis为（x，y），对应的下标为（0,1），np.transpose()传入的参数为（1,0），即将原数组的0,1轴互换。综上，对二维数组的transpose操作就是对原数组的转置操作。：{ t.transpose()}")
          
if __name__ == '__main__':
    unittest.main()