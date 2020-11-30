# fileIO.py
# -*- coding: UTF-8 -*-
#主要处理程序的基础文件地址识别、文件及文件夹操作

import os

#获取指定目录path下的png文件地址,并输出到list_name数组中
def listdir(path, list_name): 
  for file in os.listdir(path): 
    file_path = os.path.join(path, file) 
    if os.path.isdir(file_path): 
      listdir(file_path, list_name) 
    elif os.path.splitext(file_path)[1]=='.png': 
      list_name.append(file_path) 

#检测文件夹是否存在，无则创建
def initdir(name):
 if not os.path.exists(name):
  warningstr = '\n未检测到文件夹：' + name +'\n'
  print(warningstr)
  os.makedirs(name)
  makestr = name + '文件夹已创建\n'
  print(makestr)

#自动移动文件到CSL的import文件夹中---！！！未完成
def move2CSLImport():
 return
