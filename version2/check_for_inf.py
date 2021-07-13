
#检查输入信息模块
#调用函数：def check_fun(mat_path):
#返回值：none


import os

def check_fun(mat_path,tar_path):
    print('正在准备进行素材文件夹检查')
    print('请确保素材文件夹内子文件夹命名正确')
    print('以及目标路径下无重名项目文件夹')
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
    
    #素材文件夹的子文件夹路径
    fol_name_mat_pictur = mat_path + '\\' + '照片'
    fol_name_mat_video = mat_path + '\\' + '录像'

    #子文件夹列表
    flo_dir_pictur = os.listdir(fol_name_mat_pictur)
    flo_dir_video = os.listdir(fol_name_mat_video)
    #子文件夹下项目名称输出
    print(flo_dir_pictur)
    print(flo_dir_video)
    while flo_dir_pictur != flo_dir_video:
        print('素材文件夹不对应，请检查！')
        print('检查完成后请按任意键')
        os.system('pause')
        flo_dir_pictur = os.listdir(fol_name_mat_pictur)
        flo_dir_video = os.listdir(fol_name_mat_video)
    else:
        print('素材校验完成')
    
    #目标路径检查
    print('正在准备进行目标路径的检查')
    print('请确保目标路径下无重名项目文件夹')
    print('确认完成后请按任意键')
    os.system('pause')

    tar_dir = os.listdir(tar_path)
    while tar_dir != []:
        print('文件夹不为空')
        print('请再次确认，完成请按任意键')
        os.system('pause')
        tar_dir = os.listdir(tar_dir)
    else:
        print('目标目录校验成功')

