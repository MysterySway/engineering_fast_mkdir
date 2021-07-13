version = 'v0.2.0.1'

#输入：项目名称、素材文件路径、目标路径、楼号                              
#确认信息                                                   
#复制素材文件夹
#在素材文件夹内创建楼号文件夹
#创建目标文件夹
#移动楼号文件夹
#结束


#os.path.getmtime(file)最近修改时间输出时间戳
#print "time.ctime() : %s" % time.ctime()转化时间戳
#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 格式化时间

#import os,time 
#print(time.ctime(os.stat("d:/1.txt").st_mtime)) #文件的修改时间 
#time.ctime(os.stat("d:/1.txt").st_ctime) #文件的创建时间
#print(time.strftime("%Y%m%d",time.gmtime(os.path.getmtime("d:/1.txt"))))

#开始界面
print('----------')
print('欢迎使用快速创建工程影像工具')
print('版本：' + version)
print('----------\n')
print('正在加载第三方库文件')

import os
import sys
import time
import shutil

print('完成\n')

print('正在加载其他函数文件')
#输入整理函数
import input_inf_settle
#输入信息模块
#调用函数：def input_function()
#返回值 project_name：项目名称
#       staff：移交人
#       mat_path：素材文件夹路径
#       tar_path：目标文件夹路径
#       list_floor：楼号列表

#检查输入函数
import check_for_inf
#检查输入信息模块
#调用函数：def check_fun(mat_path):
#返回值：none

#复制素材函数
import copy_file
#调用函数：def copy(mat_path):
#返回值：none

#创建楼号文件夹模块
import create_flo_fol
#调用函数：def check_fun(mat_path):
#返回值：none

#移动文件夹模块
import move_file
#调用函数：def move(mat_path,target_path,project_name,staff):
#返回值：none

print('完成\n')


#主体函数调用
#输入整理函数
project_name,staff,mat_path,tar_path,list_floor = input_inf_settle.input_function()

#检查输入函数
check_for_inf.check_fun(mat_path,tar_path)

#复制素材函数
copy_file.copy(mat_path)

#创建楼号文件夹模块
create_flo_fol.cr_mome_flo(mat_path,list_floor)

#创建目标文件夹，移动文件夹函数
move_file.move(mat_path,tar_path,project_name,staff)

