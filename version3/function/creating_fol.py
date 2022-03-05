

#传参：项目名称project_name
#       建立文件夹的位置target_location_fol
#       移交人person_hands_over
#       移交日期date_hands_over

#传参测试
project_name = '中海'
target_location_fol = 'F:\\测试'
person_hands_over = '钟畅'
date_hands_over = '20211101'


#文件夹名称
top_folder_name = project_name + '项目声像档案（移交人：' + person_hands_over + '，移交日期：' + date_hands_over + '）'
sub_video_folder_name = project_name + '项目录像档案（移交人：' + person_hands_over + '，移交日期：' + date_hands_over + '）'
sub_photo_folder_name = project_name + '项目照片档案（移交人：' + person_hands_over + '，移交日期：' + date_hands_over + '）'
folder_name_main_00 = ['01、原貌及拆迁',
'02、整体外观进展及现场管理',
'03、基础',
'04、主体',
'05、防水、保温、防腐',
'06、室内管道',
'07、室外管线',
'08、电气',
'09、建筑智能',
'10、通风与空调',
'11、消防',
'12、重大事故',
'13、开工、封顶、竣工仪式及质检验收等活动',
'14、竣工面貌',
'15、内部功能、附属配套、装修及使用情况']

#文件夹路径
top_folder_path = target_location_fol + '\\' + top_folder_name
sub_video_folder_path = top_folder_path + '\\' + sub_video_folder_name
sub_photo_folder_path = top_folder_path + '\\' + sub_photo_folder_name

#创建文件夹
import os

os.chdir(target_location_fol)
os.mkdir(top_folder_name)
os.chdir(top_folder_path)
os.mkdir(sub_video_folder_name)
os.mkdir(sub_photo_folder_name)
os.chdir(sub_video_folder_path)
for i in range(len(folder_name_main_00)):
    os.mkdir(folder_name_main_00[i])
os.chdir(sub_photo_folder_path)
for i in range(len(folder_name_main_00)):
    os.mkdir(folder_name_main_00[i])

