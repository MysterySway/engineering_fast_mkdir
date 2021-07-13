version = 'v0.0.1.1 开发版'

#输入：项目名称、素材文件路径、目标路径、楼号                                     完成
#确认信息                                                                      完成
#创建暂存文件夹，命名并移动文件到暂存，按内容分文件夹
#移动文件夹
#结束
#os.path.getmtime(file)最近修改时间输出时间戳
#print "time.ctime() : %s" % time.ctime()转化时间戳
#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 格式化时间



#project_name :项目名称 str
#staff：移交人 str
#mat_path：素材路径 str
#tar_path：目标路径 str
#list_floor：楼号 list


'''
#调用输入信息函数
project_name,staff,mat_path,tar_path,list_floor = inp_inf.input_function()
print(project_name,staff,mat_path,tar_path,list_floor)
'''

print('----------')
print('欢迎使用快速创建工程影像工具')
print('版本：' + version)
print('----------\n')
print('加载第三方库文件')

import os
import sys
import time
import shutil
import cr_flo_tar_mor as cr_ftm
import input_information as inp_inf

print('成功\n')

moddle = {'1':'完整模式，完全执行所有操作','2':'只创建项目文件夹，不进行填充映像文件'}
moddle_str = '1:完整模式，完全执行所有操作\n2:只创建项目文件夹，不进行填充映像文件\n'
#模式输入
command_input = input('请选择模式：\n' + moddle_str + '>>> ')
#模式输入函数
def cmd_jud(command):
    if command == '1':
        print('完整模式\n')
        return 1
    elif command == '2':
        print('只创建模式\n')
        return 2
    else:
        print('错误，无效的命令\n')
        command_input = input('请选择模式：\n' + moddle_str + '>>> ')
        cmd_jud(command_input)

command = cmd_jud(command_input)

#def jud_flo_tar(tar_path,project_name,hand_over_person,person_who):
#project_name,staff,mat_path,tar_path,list_floor = inp_inf.input_function()

#模式选择运行
if command == 1:
    #完全模式
    
    #输入函数获取数据
    project_name,staff,mat_path,tar_path,list_floor = inp_inf.input_function()
    #创建函数创建文件夹
    base_path_dict = cr_ftm.jud_flo_tar(tar_path,project_name,staff)
    #分拣函数（没写）

elif command == 2:
    #只创建（完成）
    project_name,staff,mat_path,tar_path,list_floor = inp_inf.input_function()
    test_dict = cr_ftm.jud_flo_tar(tar_path,project_name,staff)