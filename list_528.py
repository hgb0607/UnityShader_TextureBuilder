# list_528.py
# -*- coding: UTF-8 -*-

#一维转528列表
def List528(lineList):
 list_str = [[0 for i in range(16)] for j in range(33)]
 count = 0
 for j in range(len(list_str)):
  for k in range(len(list_str[j])):
   list_str[j][k] = lineList[count]
   count += 1
 return list_str
 
#一维转斜528列表
def ListX528(lineList):
 list_str = [[0 for i in range(16)] for j in range(33)]
 a = 0
 b = 0
 for count in range(len(lineList)):
  list_str[a][b] = lineList[count]
  a += 1
  b += 1
  if a == 33:
   a = 0
  if b == 16:
   b = 0
 
 return list_str

#-----------#