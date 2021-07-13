#输入信息模块

import os

#project_name :项目名称 str
#staff：移交人 str
#mat_path：素材路径 str
#tar_path：目标路径 str
#list_floor：楼号 list

#主体函数
#输入信息模块
def input_function():
    #楼号输入函数
    def floor_sub(input_floor,list_floor):
        list_floor = []
        while input_floor != 'pass':
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

    #输入信息函数
    def input_information():
        project_name = input('请输入项目名称：')
        staff = input('输入移交人：')
        mat_path = input('请输入素材文件夹路径：')
        tar_path = input('请输入要建立文件夹的目标路径：')
        input_floor = input('输入楼号(单个)：')
        inf_list = [project_name,staff,mat_path,tar_path,input_floor]
        print(inf_list)

    #楼号函数的调用
    list_floor=floor_sub(input_floor,list_floor = [0])

    #主体信息的确定
    '''
    信息集合
    information = [project_name,material_path,target_path]+list_floor
    print(information)
    '''
    print('\n请确认信息：')
    print('项目名称：' + project_name)
    print('移交人：' + staff)
    print('素材路径：'+ mat_path)
    print('目标路径：'+ tar_path)
    print('楼号：'+ str(list_floor))
    infcom = input('\n信息是否正确？Y/N：')
    while infcom != 'Y' and infcom !='y':
        input_information()
        list_floor=floor_sub(input_floor,list_floor = [0])
        '''
        信息集合
        information = [project_name,material_path,target_path]+list_floor
        print(information)
        '''
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

input_function()