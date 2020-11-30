# list_528.py
# -*- coding: UTF-8 -*-
#将一维列表整理成二维列表(python中的列表嵌套)
#主要函数包括DiagonalList斜角排列,RegularList横排常规,默认排列528列表函数List528和ListX528
#引用参数为python的列表list = [],行数和列数(整数型)
#返回参数为python中的List嵌套列表(类似二维数组)


#斜角排列算法
#参数：lineList, row, column --- 地址列表(一维), 列数整数, 行数整数
#返回：地址列表(二维)
def DiagonalList(lineList, row, column):
 list_str = [[0 for i in range(row)] for j in range(column)]
 a = 0
 b = 0
 for count in range(len(lineList)):
  list_str[a][b] = lineList[count]
  a += 1
  b += 1
  if a == column:
   a = 0
  if b == row:
   b = 0
 return list_str

#横排常规排列算法
#参数：lineList, row, column --- 地址列表(一维), 列数整数, 行数整数
#返回：地址列表(二维)
def RegularList(lineList, row, column):
 list_str = [[0 for i in range(row)] for j in range(column)]
 count = 0
 for j in range(len(list_str)):
  for k in range(len(list_str[j])):
   list_str[j][k] = lineList[count]
   count += 1
 return list_str

#一维转斜528列表，16列33行用
def ListX528(lineList):
 list_X528 = DiagonalList(lineList, 16, 33)
 return list_X528

#一维转528列表，16列33行用
def List528(lineList):
 list_528 = RegularList(lineList, 16, 33)
 return list_528
#-----------#