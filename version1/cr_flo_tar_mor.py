#创建目标文件夹模块

import os
import time


#文件夹目录
fol_name_main_01 = '01、原貌及拆迁'
fol_name_main_02 = '02、整体外观进展及现场管理'
fol_name_main_03 = '03、基础'
fol_name_main_04 = '04、主体'
fol_name_main_05 = '05、防水、保温、防腐'
fol_name_main_06 = '06、室内管道'
fol_name_main_07 = '07、室外管线'
fol_name_main_08 = '08、电气'
fol_name_main_09 = '09、建筑智能'
fol_name_main_10 = '10、通风与空调'
fol_name_main_11 = '11、消防'
fol_name_main_12 = '12、重大事故'
fol_name_main_13 = '13、开工、封顶、竣工仪式及质检验收等活动'
fol_name_main_14 = '14、竣工面貌'
fol_name_main_15 = '15、内部功能、附属配套、装修及使用情况'


#传参：目标文件夹路径,项目名称，移交人，拍摄人，移交日期，
#输出：最终目标目录起始路径，目标文件夹列表

def cr_flo_tar_mor(tar_path,project_name,hand_over_person):
    print('目标文件夹已确认为:',tar_path)
    print('命名最上层文件夹名称')
    tar_base_flo_name = project_name + '工程声像档案（移交人：' + hand_over_person + '，' + '移交日期：'+ time.strftime('%Y.%m.%d',time.localtime()) +')'
    print('切换目录')
    os.chdir(tar_path)
    print('创建最上层文件夹')
    os.mkdir(tar_base_flo_name)
    print('文件夹已创建，名称：',tar_base_flo_name)

    print('次级文件夹路径')
    tar_path_next = tar_path + '\\' + tar_base_flo_name
    print('切换目录')
    os.chdir(tar_path_next)
    print('命名次级文件夹')
    tar_base_flo_pictur = project_name +'工程照片档案（移交人：'+ hand_over_person +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
    tar_base_flo_video = project_name +'工程录像档案（移交人：'+ hand_over_person +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
    print('第二次级文件夹路径')
    tar_path_main_pictur = tar_path_next + '\\' + tar_base_flo_pictur
    tar_path_main_video = tar_path_next + '\\' + tar_base_flo_video
    print('创建次级文件夹')
    os.mkdir(tar_path_main_pictur)
    os.mkdir(tar_path_main_video)
    print('次级文件夹目录已创建，名称：',tar_base_flo_pictur,tar_base_flo_video)

    print('切换目录')
    os.chdir(tar_path_main_pictur)
    print('创建文件夹')
    os.mkdir(fol_name_main_01)
    os.mkdir(fol_name_main_02)
    os.mkdir(fol_name_main_03)
    os.mkdir(fol_name_main_04)
    os.mkdir(fol_name_main_05)
    os.mkdir(fol_name_main_06)
    os.mkdir(fol_name_main_07)
    os.mkdir(fol_name_main_08)
    os.mkdir(fol_name_main_09)
    os.mkdir(fol_name_main_10)
    os.mkdir(fol_name_main_11)
    os.mkdir(fol_name_main_12)
    os.mkdir(fol_name_main_13)
    os.mkdir(fol_name_main_14)
    os.mkdir(fol_name_main_15)
    print('照片文件夹创建完成')

    print('切换目录')
    os.chdir(tar_path_main_video)
    print('创建文件夹')
    os.mkdir(fol_name_main_01)
    os.mkdir(fol_name_main_02)
    os.mkdir(fol_name_main_03)
    os.mkdir(fol_name_main_04)
    os.mkdir(fol_name_main_05)
    os.mkdir(fol_name_main_06)
    os.mkdir(fol_name_main_07)
    os.mkdir(fol_name_main_08)
    os.mkdir(fol_name_main_09)
    os.mkdir(fol_name_main_10)
    os.mkdir(fol_name_main_11)
    os.mkdir(fol_name_main_12)
    os.mkdir(fol_name_main_13)
    os.mkdir(fol_name_main_14)
    os.mkdir(fol_name_main_15)
    print('录像文件夹创建完成')

    #最低级文件夹路径
    last_path_pictur_01 = tar_path_main_pictur + '\\' + fol_name_main_01
    last_path_pictur_02 = tar_path_main_pictur + '\\' + fol_name_main_02
    last_path_pictur_03 = tar_path_main_pictur + '\\' + fol_name_main_03
    last_path_pictur_04 = tar_path_main_pictur + '\\' + fol_name_main_04
    last_path_pictur_05 = tar_path_main_pictur + '\\' + fol_name_main_05
    last_path_pictur_06 = tar_path_main_pictur + '\\' + fol_name_main_06
    last_path_pictur_07 = tar_path_main_pictur + '\\' + fol_name_main_07
    last_path_pictur_08 = tar_path_main_pictur + '\\' + fol_name_main_08
    last_path_pictur_09 = tar_path_main_pictur + '\\' + fol_name_main_09
    last_path_pictur_10 = tar_path_main_pictur + '\\' + fol_name_main_10
    last_path_pictur_11 = tar_path_main_pictur + '\\' + fol_name_main_11
    last_path_pictur_12 = tar_path_main_pictur + '\\' + fol_name_main_12
    last_path_pictur_13 = tar_path_main_pictur + '\\' + fol_name_main_13
    last_path_pictur_14 = tar_path_main_pictur + '\\' + fol_name_main_14
    last_path_pictur_15 = tar_path_main_pictur + '\\' + fol_name_main_15

    last_path_video_01 = tar_path_main_video + '\\' + fol_name_main_01
    last_path_video_02 = tar_path_main_video + '\\' + fol_name_main_02
    last_path_video_03 = tar_path_main_video + '\\' + fol_name_main_03
    last_path_video_04 = tar_path_main_video + '\\' + fol_name_main_04
    last_path_video_05 = tar_path_main_video + '\\' + fol_name_main_05
    last_path_video_06 = tar_path_main_video + '\\' + fol_name_main_06
    last_path_video_07 = tar_path_main_video + '\\' + fol_name_main_07
    last_path_video_08 = tar_path_main_video + '\\' + fol_name_main_08
    last_path_video_09 = tar_path_main_video + '\\' + fol_name_main_09
    last_path_video_10 = tar_path_main_video + '\\' + fol_name_main_10
    last_path_video_11 = tar_path_main_video + '\\' + fol_name_main_11
    last_path_video_12 = tar_path_main_video + '\\' + fol_name_main_12
    last_path_video_13 = tar_path_main_video + '\\' + fol_name_main_13
    last_path_video_14 = tar_path_main_video + '\\' + fol_name_main_14
    last_path_video_15 = tar_path_main_video + '\\' + fol_name_main_15
    
    #文件夹路径树字典
    tar_path_dict = {'目标文件夹主路径':tar_path_next,'照片文件夹路径':tar_path_main_pictur,'录像文件夹路径':tar_path_main_video,'last_path_pictur_01':last_path_pictur_01,'last_path_pictur_02':last_path_pictur_02,'last_path_pictur_03':last_path_pictur_03,'last_path_pictur_04':last_path_pictur_04,'last_path_pictur_05':last_path_pictur_05,'last_path_pictur_06':last_path_pictur_06,'last_path_pictur_07':last_path_pictur_07,'last_path_pictur_08':last_path_pictur_08,'last_path_pictur_09':last_path_pictur_09,'last_path_pictur_10':last_path_pictur_10,'last_path_pictur_11':last_path_pictur_11,'last_path_pictur_12':last_path_pictur_12,'last_path_pictur_13':last_path_pictur_13,'last_path_pictur_14':last_path_pictur_14,'last_path_pictur_15':last_path_pictur_15,'last_path_video_01':last_path_video_01,'last_path_video_02':last_path_video_02,'last_path_video_03':last_path_video_03,'last_path_video_04':last_path_video_04,'last_path_video_05':last_path_video_05,'last_path_video_06':last_path_video_06,'last_path_video_07':last_path_video_07,'last_path_video_08':last_path_video_08,'last_path_video_09':last_path_video_09,'last_path_video_10':last_path_video_10,'last_path_video_11':last_path_video_11,'last_path_video_12':last_path_video_12,'last_path_video_13':last_path_video_13,'last_path_video_14':last_path_video_14,'last_path_video_15':last_path_video_15}
    return tar_path_dict


#主题函数
#判断文件夹内是否已经存在文件夹
#创建目标文件夹模块
#传参：目标文件夹路径,项目名称，移交人
#输出：目标文件夹路径列表


def jud_flo_tar(tar_path,project_name,hand_over_person):
    list1 = os.listdir(tar_path)
    list2 = []
    if list1 != list2:
        print('已有文件夹，请删除现有文件夹或者跳过此步')
        base_dict = {}
    else:
        base_dict = {}
        base_dict = cr_flo_tar_mor(tar_path,project_name,hand_over_person)
    return base_dict