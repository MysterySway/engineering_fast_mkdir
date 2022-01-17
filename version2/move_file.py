#移动文件夹模块
#调用函数：def move(mat_path,target_path,project_name,staff):
#返回值：none


import os
import shutil
import time

def move(mat_path,target_path,project_name,staff):
    #文件夹名称
    folder_name_main_01 = '01、原貌及拆迁'
    folder_name_main_02 = '02、整体外观进展及现场管理'
    folder_name_main_03 = '03、基础'
    folder_name_main_04 = '04、主体'
    folder_name_main_05 = '05、防水、保温、防腐'
    folder_name_main_06 = '06、室内管道'
    folder_name_main_07 = '07、室外管线'
    folder_name_main_08 = '08、电气'
    folder_name_main_09 = '09、建筑智能'
    folder_name_main_10 = '10、通风与空调'
    folder_name_main_11 = '11、消防'
    folder_name_main_12 = '12、重大事故'
    folder_name_main_13 = '13、开工、封顶、竣工仪式及质检验收等活动'
    folder_name_main_14 = '14、竣工面貌'
    folder_name_main_15 = '15、内部功能、附属配套、装修及使用情况'

    print('目标路径',target_path,'正在切换工作目录')
    os.chdir(target_path)
    print('当前工作文件夹',os.getcwd())
    print('\n正在准备向目标文件夹中创建主体框架\n')

    #要创建的文件夹列表
    print('创建工程文件夹')
    project_name_add = project_name +'工程声像档案（移交人：'+ staff +'，移交日期：' + time.strftime('%Y.%m.%d',time.localtime()) +')'              #创建人
    os.mkdir(project_name_add)
    target_path_main =target_path +'\\'+ project_name_add
    print('切换目录')
    os.chdir(target_path_main)
    print('当前工作文件夹',os.getcwd())

    print('创建次级文件夹')
    folder_name_main_pictur = project_name +'工程照片档案（移交人：'+ staff +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
    folder_name_main_video = project_name +'工程录像档案（移交人：'+ staff +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
    target_path_main_pictur = target_path_main + '\\' + folder_name_main_pictur
    target_path_main_video = target_path_main + '\\' + folder_name_main_video
    os.mkdir(folder_name_main_pictur)
    os.mkdir(folder_name_main_video)
    print('当前工作文件夹',os.getcwd())

    print('切换目录')
    os.chdir(target_path_main_pictur)
    print('当前工作文件夹',os.getcwd())
    os.mkdir(folder_name_main_01)
    os.mkdir(folder_name_main_02)
    os.mkdir(folder_name_main_03)
    os.mkdir(folder_name_main_04)
    os.mkdir(folder_name_main_05)
    os.mkdir(folder_name_main_06)
    os.mkdir(folder_name_main_07)
    os.mkdir(folder_name_main_08)
    os.mkdir(folder_name_main_09)
    os.mkdir(folder_name_main_10)
    os.mkdir(folder_name_main_11)
    os.mkdir(folder_name_main_12)
    os.mkdir(folder_name_main_13)
    os.mkdir(folder_name_main_14)
    os.mkdir(folder_name_main_15)

    print('切换目录')
    os.chdir(target_path_main_video)
    print('当前工作文件夹',os.getcwd())
    os.mkdir(folder_name_main_01)
    os.mkdir(folder_name_main_02)
    os.mkdir(folder_name_main_03)
    os.mkdir(folder_name_main_04)
    os.mkdir(folder_name_main_05)
    os.mkdir(folder_name_main_06)
    os.mkdir(folder_name_main_07)
    os.mkdir(folder_name_main_08)
    os.mkdir(folder_name_main_09)
    os.mkdir(folder_name_main_10)
    os.mkdir(folder_name_main_11)
    os.mkdir(folder_name_main_12)
    os.mkdir(folder_name_main_13)
    os.mkdir(folder_name_main_14)
    os.mkdir(folder_name_main_15)

    #照片文件夹路径
    folder_name_pictur_01 = target_path_main_pictur + '\\' + folder_name_main_01
    folder_name_pictur_02 = target_path_main_pictur + '\\' + folder_name_main_02
    folder_name_pictur_03 = target_path_main_pictur + '\\' + folder_name_main_03
    folder_name_pictur_04 = target_path_main_pictur + '\\' + folder_name_main_04
    folder_name_pictur_05 = target_path_main_pictur + '\\' + folder_name_main_05
    folder_name_pictur_06 = target_path_main_pictur + '\\' + folder_name_main_06
    folder_name_pictur_07 = target_path_main_pictur + '\\' + folder_name_main_07
    folder_name_pictur_08 = target_path_main_pictur + '\\' + folder_name_main_08
    folder_name_pictur_09 = target_path_main_pictur + '\\' + folder_name_main_09
    folder_name_pictur_10 = target_path_main_pictur + '\\' + folder_name_main_10
    folder_name_pictur_11 = target_path_main_pictur + '\\' + folder_name_main_11
    folder_name_pictur_12 = target_path_main_pictur + '\\' + folder_name_main_12
    folder_name_pictur_13 = target_path_main_pictur + '\\' + folder_name_main_13
    folder_name_pictur_14 = target_path_main_pictur + '\\' + folder_name_main_14
    folder_name_pictur_15 = target_path_main_pictur + '\\' + folder_name_main_15

    #录像文件夹路径
    folder_name_video_01 = target_path_main_video + '\\' + folder_name_main_01
    folder_name_video_02 = target_path_main_video + '\\' + folder_name_main_02
    folder_name_video_03 = target_path_main_video + '\\' + folder_name_main_03
    folder_name_video_04 = target_path_main_video + '\\' + folder_name_main_04
    folder_name_video_05 = target_path_main_video + '\\' + folder_name_main_05
    folder_name_video_06 = target_path_main_video + '\\' + folder_name_main_06
    folder_name_video_07 = target_path_main_video + '\\' + folder_name_main_07
    folder_name_video_08 = target_path_main_video + '\\' + folder_name_main_08
    folder_name_video_09 = target_path_main_video + '\\' + folder_name_main_09
    folder_name_video_10 = target_path_main_video + '\\' + folder_name_main_10
    folder_name_video_11 = target_path_main_video + '\\' + folder_name_main_11
    folder_name_video_12 = target_path_main_video + '\\' + folder_name_main_12
    folder_name_video_13 = target_path_main_video + '\\' + folder_name_main_13
    folder_name_video_14 = target_path_main_video + '\\' + folder_name_main_14
    folder_name_video_15 = target_path_main_video + '\\' + folder_name_main_15

    #对素材文件夹进行操作
    #mat_path:根文件夹
    mome_flo_path = mat_path + '\\' + 'mome_flo'
    mome_flo_pictur = mome_flo_path + '\\' + '照片'
    mome_flo_video = mome_flo_path + '\\' + '录像'

    #文件夹名称
    '''
    folder_name_main_01 = '01、原貌及拆迁'
    folder_name_main_02 = '02、整体外观进展及现场管理'
    folder_name_main_03 = '03、基础'
    folder_name_main_04 = '04、主体'
    folder_name_main_05 = '05、防水、保温、防腐'
    folder_name_main_06 = '06、室内管道'
    folder_name_main_07 = '07、室外管线'
    folder_name_main_08 = '08、电气'
    folder_name_main_09 = '09、建筑智能'
    folder_name_main_10 = '10、通风与空调'
    folder_name_main_11 = '11、消防'
    folder_name_main_12 = '12、重大事故'
    folder_name_main_13 = '13、开工、封顶、竣工仪式及质检验收等活动'
    folder_name_main_14 = '14、竣工面貌'
    folder_name_main_15 = '15、内部功能、附属配套、装修及使用情况'
    '''
    #移动函数
    def move_fil_with_flo(start_path,goal_path):
        fil_path_list = os.listdir(start_path)
        for i in fil_path_list:
            fil_path_flo = start_path + '\\' + i
            shutil.move(fil_path_flo,goal_path)

    #照片操作
    print('正在移动照片')
    mome_pictur_flo_list = os.listdir(mome_flo_pictur)
    for project in mome_pictur_flo_list:
        project_path = mome_flo_pictur + '\\' + project
        if project == '屋面防水':
            move_fil_with_flo(project_path,folder_name_pictur_05)
        elif project == '卫生间地面防水':
            move_fil_with_flo(project_path,folder_name_pictur_05)
        
        elif project == '分水器':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '给水管道':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '给水管线':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '燃气管道':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '燃气管线':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '排水管道':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '排水管线':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '供暖管道':
            move_fil_with_flo(project_path,folder_name_pictur_06)
        elif project == '供暖管道井':
            move_fil_with_flo(project_path,folder_name_pictur_06)

        elif project == '外排水':
            move_fil_with_flo(project_path,folder_name_pictur_07)

        elif project == '插座':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '开关':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '电梯':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '电梯间':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '多媒体箱':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '弱电箱':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '照明':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '防雷':
            move_fil_with_flo(project_path,folder_name_pictur_08)
        elif project == '分户箱':
            move_fil_with_flo(project_path,folder_name_pictur_08)

        elif project == '可视通话':
            move_fil_with_flo(project_path,folder_name_pictur_09)
        elif project == '单元可视通话':
            move_fil_with_flo(project_path,folder_name_pictur_09)

        elif project == '屋面排风':
            move_fil_with_flo(project_path,folder_name_pictur_10)
        elif project == '通风管道':
            move_fil_with_flo(project_path,folder_name_pictur_10)
        elif project == '通风管线':
            move_fil_with_flo(project_path,folder_name_pictur_10)

        elif project == '安全出口指示牌':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '光感报警器':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '火灾报警器':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '消火栓':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '烟感报警器':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '消火栓':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '喷淋':
            move_fil_with_flo(project_path,folder_name_pictur_11)
        elif project == '消防应急灯':
            move_fil_with_flo(project_path,folder_name_pictur_11)

        elif project == '竣工外貌':
            move_fil_with_flo(project_path,folder_name_pictur_14)

        elif project == '单元门':
            move_fil_with_flo(project_path,folder_name_pictur_15)
        elif project == '室内环境':
            move_fil_with_flo(project_path,folder_name_pictur_15)
    print('移动完成')
    
    #录像操作
    print('正在移动视频')
    mome_video_flo_list = os.listdir(mome_flo_video)
    for project in mome_video_flo_list:
        project_path = mome_flo_video + '\\' + project
        if project == '屋面防水':
            move_fil_with_flo(project_path,folder_name_video_05)
        elif project == '卫生间地面防水':
            move_fil_with_flo(project_path,folder_name_video_05)
        
        elif project == '分水器':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '给水管道':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '给水管线':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '燃气管道':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '燃气管线':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '排水管道':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '排水管线':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '供暖管道':
            move_fil_with_flo(project_path,folder_name_video_06)
        elif project == '供暖管道井':
            move_fil_with_flo(project_path,folder_name_video_06)

        elif project == '外排水':
            move_fil_with_flo(project_path,folder_name_video_07)

        elif project == '插座':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '开关':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '电梯':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '电梯间':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '多媒体箱':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '弱电箱':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '照明':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '防雷':
            move_fil_with_flo(project_path,folder_name_video_08)
        elif project == '分户箱':
            move_fil_with_flo(project_path,folder_name_video_08)

        elif project == '可视通话':
            move_fil_with_flo(project_path,folder_name_video_09)
        elif project == '单元可视通话':
            move_fil_with_flo(project_path,folder_name_video_09)
        elif project == '智能通话':
            move_fil_with_flo(project_path,folder_name_video_09)
        elif project == '单元智能通话':
            move_fil_with_flo(project_path,folder_name_video_09)


        elif project == '屋面排风':
            move_fil_with_flo(project_path,folder_name_video_10)
        elif project == '通风管道':
            move_fil_with_flo(project_path,folder_name_video_10)
        elif project == '通风管线':
            move_fil_with_flo(project_path,folder_name_video_10)

        elif project == '安全出口指示牌':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '光感报警器':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '火灾报警器':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '消火栓':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '烟感报警器':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '消火栓':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '喷淋':
            move_fil_with_flo(project_path,folder_name_video_11)
        elif project == '消防应急灯':
            move_fil_with_flo(project_path,folder_name_video_11)

        elif project == '竣工外貌':
            move_fil_with_flo(project_path,folder_name_video_14)

        elif project == '单元门':
            move_fil_with_flo(project_path,folder_name_video_15)
        elif project == '室内环境':
            move_fil_with_flo(project_path,folder_name_video_15)
    print('完成')



