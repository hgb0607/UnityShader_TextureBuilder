# fileIO.py
# -*- coding: UTF-8 -*-

import os

def listdir(path, list_name): 
  for file in os.listdir(path): 
    file_path = os.path.join(path, file) 
    if os.path.isdir(file_path): 
      listdir(file_path, list_name) 
    elif os.path.splitext(file_path)[1]=='.png': 
      list_name.append(file_path) 
# return list_name

def initdir(name):
 if not os.path.exists(name):
  warningstr = '\n未检测到文件夹：' + name +'\n'
  print(warningstr)
  os.makedirs(name)
  makestr = name + '文件夹已创建\n'
  print(makestr)
#  input('调试中断')

def move2CSLImport():
 return
