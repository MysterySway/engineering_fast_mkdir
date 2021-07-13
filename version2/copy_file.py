




#复制素材函数
#调用函数：def copy(mat_path):
#返回值：none




import shutil
import os

def copy(mat_path):
    #创建备份文件夹
    print('正在准备备份素材文件夹')
    os.chdir(mat_path)
    fol_name_mat_pictur = mat_path + '\\' + '照片'
    fol_name_mat_video = mat_path + '\\' + '录像'
    fol_name_mat_backups_pictur = mat_path + '\\' + '备份照片素材文件夹'
    fol_name_mat_backups_video = mat_path + '\\' + '备份录像素材文件夹'
    shutil.copytree(fol_name_mat_pictur,fol_name_mat_backups_pictur)
    shutil.copytree(fol_name_mat_video,fol_name_mat_backups_video)
    print('备份完成')

