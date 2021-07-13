
#创建楼号文件夹模块
#调用函数：def check_fun(mat_path):
#返回值：none

import os
import shutil
import time


def cr_mome_flo(mat_path,list_floor):
    #素材文件夹的子文件夹路径
    print('创建中转文件夹')
    fol_path_mat_pictur = mat_path + '\\' + '照片'
    fol_path_mat_video = mat_path + '\\' + '录像'
    
    #创建暂存文件夹
    os.chdir(mat_path)
    os.mkdir('mome_flo')
    mome_flo_path = mat_path + '\\' + 'mome_flo'
    os.chdir(mome_flo_path)
    os.mkdir('照片')
    os.mkdir('录像')
    
    #暂存文件夹路径
    mome_flo_pictur = mome_flo_path + '\\' + '照片'
    mome_flo_video = mome_flo_path + '\\' + '录像'

    #复制文件夹内项目文件夹到临时目录
    flo_dir_mat_pictur = os.listdir(fol_path_mat_pictur)
    flo_dir_mat_video = os.listdir(fol_path_mat_video)
    os.chdir(mome_flo_pictur)
    for i in flo_dir_mat_pictur:
        os.mkdir(i)
    os.chdir(mome_flo_video)
    for i in flo_dir_mat_video:
        os.mkdir(i)
    #识别项目名称，在分拣目录创建文件夹
    #命名文件夹
    #                           文件路径            楼号        文件上级目录            项目名称
    def material_folder_name(material_path_name,floor_number,parent_directory_path,directory_name):
        date_variable = time.strftime("%Y%m%d",time.gmtime(os.path.getmtime(material_path_name)))
        name_variable = date_variable + '_' + floor_number + '#' + directory_name + '（拍摄人：钟畅）'
        os.chdir(parent_directory_path)
        os.mkdir(name_variable)
        destination_folder_path = parent_directory_path + '\\' + name_variable
        shutil.move(material_path_name,destination_folder_path)
        return destination_folder_path

    #循环进行重命名与移动
    #                    项目主路径         暂存目标主路径     楼号列表
    def rename_and_move(main_project_path,main_mome_path,list_floor):    
        mat_flo = os.listdir(main_project_path)
        for flo in mat_flo:
            progect_path = main_project_path + '\\' + flo
            for floor_number in list_floor:
                os.chdir(progect_path)
                material_path_name_list =  os.listdir(progect_path)
                material_path_name_list_path0 = progect_path + '\\' + material_path_name_list[0]
                destination_folder_path = material_folder_name(material_path_name_list_path0,floor_number,progect_path,flo)
                main_mome_flo_path_list = os.listdir(main_mome_path)
                pick_floor_number_path = main_mome_path + '\\' + main_mome_flo_path_list[mat_flo.index(flo)]
                shutil.move(destination_folder_path,pick_floor_number_path)
    print('移动文件到中转文件夹')
    rename_and_move(fol_path_mat_pictur,mome_flo_pictur,list_floor)
    rename_and_move(fol_path_mat_video,mome_flo_video,list_floor)



