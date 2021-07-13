#创建单个楼的所有文件夹

import os
import shutil
import time

#project_name :项目名称 str
#staff：移交人 str
#mat_path：素材路径 str
#tar_path：目标路径 str
#list_floor：楼号 list


#传参：素材文件夹根目录，楼号列表，目标文件夹路径字典
#返回值：无




def cr_mome_flo(mat_path,list_floor,base_path_dict):
    print('必须存在“录像”和“照片”文件夹在素材文件根目录下')
    print('将影像文件按种类放在两文件夹下')
    print('确认完成后请按任意键')
    os.system('pause')

    ##素材文件夹操作
    fol_dir = os.listdir(mat_path)

    #校验根目录文件夹
    while '录像' and '照片' not in fol_dir:
        print('缺少录像或者照片文件夹')
        print('请再次确认，完成请按任意键')
        os.system('pause')
        fol_dir = os.listdir(mat_path)
    else:
        print('素材根目录校验成功')
    
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
    #素材文件夹的子文件夹路径
    fol_name_mat_pictur = mat_path + '\\' + '照片'
    fol_name_mat_video = mat_path + '\\' + '录像'


    #命名文件夹
    def material_folder_name(material_path_name,floor_number,parent_directory_path,directory_name):
        date_variable = time.strftime("%Y%m%d",time.gmtime(os.path.getmtime(material_path_name)))
        name_variable = date_variable + '_' + floor_number + '#' + directory_name + '（拍摄人：钟畅）'
        os.chdir(parent_directory_path)
        os.mkdir(name_variable)
        destination_folder_path = parent_directory_path + '\\' + name_variable
        shutil.move(material_path_name,destination_folder_path)
        return destination_folder_path





















