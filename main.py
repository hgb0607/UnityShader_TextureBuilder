# main.py
# -*- coding: UTF-8 -*-
import sewImage
import fileIO
import list_528
import os
from PIL import Image

input_PATH = './input/'
outputFile_PATH = './AnimDisplay_d.png'
#test_file = './input/test.png'

#指定主程序入口
def main():
 AMU528()

#初始化程序,引导文件的导入
def initprogram():
 print('\n\n------程序开发：机智小小彪------\n\n')
 fileIO.initdir('input')
 print('请将待处理文件拷贝至input文件夹中...')
 input('复制完成后，按下回车继续处理...')

#528斜排拼图
def AMU528():
 initprogram()
 fileList = list_file(input_PATH)
 if len(fileList) == 528:
  finish_image = sewImage.sew2D(list_528.ListX528(fileList))
  print('请勿退出，正在保存文件... ...')
  finish_image.save(outputFile_PATH)
  input('\n文件已成功保存，按下回车退出程序')
 else:
  print('\n请核查导入的文件数量！')
  input('\n按下回车退出程序')


#-----------测试代码-----------#

#文件读取--测试
def list_file(path):
 Flist = []
 fileIO.listdir(path,Flist)
# print(Flist)
 return Flist

 
#用图片浏览器显示图片--测试
#参数：str --- 地址字符串
def showImage( str ):
 img = Image.open( str )
 img.show()
 print(img)
 
#528列表--测试
def List2D():
 list_tree = [[0 for i in range(16)] for j in range(33)]
 nameNum = 1

 a = 0
 b = 0
 for count in range(528):
  list_tree[a][b] = str(nameNum).zfill(3)
  nameNum += 1
  a += 1
  b += 1
  if a == 33:
   a = 0
  if b == 16:
   b = 0

# for j in range(len(list_tree)):
#  for k in range(len(list_tree[j])):
#   list_tree[j][k] = str(nameNum).zfill(3)
#   nameNum += 1

 for k in range(len(list_tree)):           #换行显示数组
  print(list_tree[k])

#-----------测试代码-----------#


#懂的都懂，没什么好说的
if __name__ == "__main__":
 main()