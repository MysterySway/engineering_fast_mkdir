
#传参：素材文件夹路径material_folder_path
        #json文件名称json_file_name
#返回：素材文件夹下所有文件的路径material_file_path_dict



#传参测试
top = 'F:\\测试'
json_file_name = 'data.json'

#遍历文件夹
import  os
original_file_path_dict = os.walk(top ,topdown=True, onerror=None, followlinks=False)

material_file_path_dict = {}

for path,dir_list,file_list in original_file_path_dict:
    for file_name in file_list:     #仅文件路径
        file_path = os.path.join(path, file_name)
        material_file_path_dict[file_name] = file_path

#写入json文件
import  json
json_file_path = 'D:\\allworkspace\\engineering_fast_mkdir\\version3\\data\\' + json_file_name

with open(json_file_path, 'w') as f:
    json.dump(material_file_path_dict,f,sort_keys=True, indent=4)


