# sewImage.py
# -*- coding: UTF-8 -*-
#图片拼接
#主要函数包括sewRow横向合并,sewColumn纵向合并,sew2D横纵矩阵合并
#引用参数为python的列表list = [],其中横纵矩阵合并时需要二维列表,列表中的数据为str全路径字符串
#返回参数为PIL中的Image对象

from PIL import Image

#横向拼接-地址式
#参数：pathList --- 图像地址列表(Py中的列表)
#返回：Image对象
def sewRow(pathList):
 print('--------------------------------')
 print('|         横向拼接程序         |')
 print('--------------------------------',end = '\n\n')
 image_objectList = loadImage(pathList)
 complete_image = sewRowImage(image_objectList)
 print('\n\n------------合并完成------------\n')
 return complete_image
  
#纵向拼接-地址式
#参数：pathList --- 图像地址列表(Py中的列表)
#返回：Image对象
def sewColumn(pathList):
 print('--------------------------------')
 print('|         纵向拼接程序         |')
 print('--------------------------------',end = '\n\n')
 image_objectList = loadImage(pathList)
 complete_image = sewColumnImage(image_objectList)
 print('\n\n------------合并完成------------\n')
 return complete_image
 
#二维拼接-地址式
#参数：pathList2D --- 图像地址列表(二维)
#返回：Image对象
def sew2D(pathList2D):
 print('--------------------------------')
 print('|         横纵拼接程序         |')
 print('--------------------------------',end = '\n\n')
 rowImages = []
 for j in range(len(pathList2D)):                           #提取二维列表每行地址
  rowImages.append(sewRowImage(loadImage(pathList2D[j])))   #行合成对象存入数组(存入<-合成<-读取<-地址)
  print('正在合并第' + str(j+1) + '行图片...',end='\r')
 complete_image = sewColumnImage(rowImages)                 #合成每行图像并返回最终对象
 print('\n\n------------合并完成------------\n')
 return complete_image

#----------------Image对象拼接----------------#

#横向拼接
#参数：imgs --- 图像对象列表(Py中的列表)
#返回：Image对象
def sewRowImage(imgs):
 width = imgs[0].size[0]     #读取图片的宽度，取数组中图一
 height = imgs[0].size[1]    #读取图片的宽度，取数组中图一
 count = len(imgs)
 target = Image.new('RGB', (width * count, height))    #创建新图片大小
 
 for i in range(count):
  left = width * i             #图片左边距离
  top = 0                      #图片顶边距离
  right = width * (i + 1)      #图片右边距离
  bottom = height              #图片底边距离
  target.paste(imgs[i],(left, top, right, bottom))
#  print('正在合并第' + str(i+1) + '张图...',end='\r')
 return target

#纵向拼接
#参数：imgs --- 图像对象列表(Py中的列表)
#返回：Image对象
def sewColumnImage(imgs):
 width = imgs[0].size[0]     #读取图片的宽度，取数组中图一
 height = imgs[0].size[1]    #读取图片的宽度，取数组中图一
 count = len(imgs)
 target = Image.new('RGB', (width, height * count))    #创建新图片大小
 
 for i in range(count):
  left = 0                     #图片左边距离
  top = height * i             #图片顶边距离
  right = width                #图片右边距离
  bottom = height * (i + 1)             #图片底边距离
  target.paste(imgs[i],(left, top, right, bottom))
#  print('正在合并第' + str(i + 1) + '张图...',end='\r')
 return target
 
#-------------Image对象拼接---end-------------#
 
#载入图像，将读取文件转换为Image对象
#参数：文件地址列表(完整路径)
#返回：Image对象列表
def loadImage(pathStrList):
 images = []            #创建Image对象列表
 for i in range(len(pathStrList)):
#  print('正在载入图片...',end='\r')
  images.append(Image.open(pathStrList[i]))
  i += 1
# print('载入完成',end='\r')
 return images
 
 
#test code
def do():
 input_PATH = './input/'
 output_PATH = './output/'
 #index = 0
 
 list_tree = [[0 for i in range(16)] for j in range(33)]
 for j in range(len(list_tree)):
  for k in range(len(list_tree[j])):
   list_tree[j][k] = './input/test.png'

 print(list_tree)

# list_tree = ['./input/test.png', './input/test.png', './input/test.png', './input/test.png']

# final_Iamge = sew2D(list_tree)
# final_Iamge.show()
 print('请勿退出，正在保存文件...')
# final_Iamge.save(output_PATH + 'finish_2D.png')
 print('已保存')
 

#-----# 
