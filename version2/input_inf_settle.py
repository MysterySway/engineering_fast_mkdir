


#输入信息模块
#调用函数：def input_function()
#返回值 project_name：项目名称
#       staff：移交人
#       mat_path：素材文件夹路径
#       tar_path：目标文件夹路径
#       list_floor：楼号列表

import os

def input_function():
    #楼号输入函数
    def floor_sub(input_floor,list_floor):
        list_floor = []
        while input_floor != 'pass' :
            list_floor.append(input_floor)
            input_floor = input('请继续输入楼号，退出请输入pass：')
        else:
            pass
        return list_floor


    project_name    = input('输入项目名称：')
    staff = input('输入移交人：')
    mat_path   = input('输入素材文件夹路径：')
    tar_path     = input('输入要建立文件夹的目标路径：')
    input_floor     = input('输入楼号(单个)：')
    
    #楼号函数的调用
    list_floor=floor_sub(input_floor,list_floor = [0])
    
    #输入信息函数
    def input_information():
        project_name = input('请输入项目名称：')
        staff = input('输入移交人：')
        mat_path = input('请输入素材文件夹路径：')
        tar_path = input('请输入要建立文件夹的目标路径：')
        input_floor = input('输入楼号(单个)：')
        list_floor = floor_sub(input_floor,list_floor = [0])
        inf_list = [project_name,staff,mat_path,tar_path,input_floor,list_floor]
        return inf_list

    #主体信息的确定
    print('\n请确认信息：')
    print('项目名称：' + project_name)
    print('移交人：' + staff)
    print('素材路径：'+ mat_path)
    print('目标路径：'+ tar_path)
    print('楼号：'+ str(list_floor))
    infcom = input('\n信息是否正确？Y/N：')
    while infcom != 'Y' and infcom !='y':
        inf_list = input_information()
        project_name,staff,mat_path,tar_path,input_floor,list_floor = inf_list
        #循环确认信息
        print('\n请确认信息：')
        print('项目名称：' + project_name)
        print('移交人：' + staff)
        print('素材路径：'+ mat_path)
        print('目标路径：'+ tar_path)
        print('楼号：'+ str(list_floor))
        infcom = input('\n信息是否正确？Y/N：')
    else:
        print('\n信息已确认\n')
    return project_name,staff,mat_path,tar_path,list_floor
