import os
import collections

path = input('Enter Path: ')
# C:\Users\Dabba\Desktop\GUI\test

EXT_DOCS = ['doc', 'docx', 'docm', 'obt', 'txt', 'csv', 'xls', 'xlsx', 'xlsm', 'pdf', 'ppt', 'pptx','pptm', 'mobi', 'epub', 'cbr']
EXT_FONT = ['ttf', 'otf']
EXT_WEB = ['html', 'css', 'scss', 'js']
EXT_AUDIO = ['wav', 'flac', 'aac', 'ogg']
EXT_VIDEO = ['3gp', 'avi', 'flv', 'mp4', 'mkv', 'mpeg']
EXT_IMAGES = ['jpeg', 'jpg', 'png', 'gif']
EXT_MUSIC = ['mp3']
EXT_ARCHIVE = ['7z', 'zip', 'rar', 'iso']
EXT_INSTALLER = ['apk', 'exe', ]
EXT_Graphics = ['abr', 'aia', 'ase', 'atn', 'eps', 'psd', 'ai', 'svg']
EXT_CODING = ['py', 'c']


os.chdir(path)
# print(os.getcwd())
srcpath = os.getcwd()

dstn_dirs = ['Pictures', 'Audio', 'Video', 'Music', 'Documents', 'Others', 'WebFiles', 'Graphics', 'Coding']

for d in dstn_dirs:
    dir_path = os.path.join(srcpath, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


file_mapping = collections.defaultdict(list)
f_list = os.listdir(srcpath)

for f_name in f_list:
    if f_name[0] != '.':
        f_ext = f_name.split('.')[-1]
        file_mapping[f_ext].append(f_name)


for f_ext, f_list in file_mapping.items():
    # print(f_ext)
    # print(f_list)
    if f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))

    elif f_ext in EXT_FONT:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))

    elif f_ext in EXT_ARCHIVE or f_ext in EXT_INSTALLER:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))

    elif f_ext in EXT_WEB:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'WebFiles', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Audio', file))

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Video', file))

    elif f_ext in EXT_IMAGES:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Pictures', file))

    elif f_ext in EXT_MUSIC:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Music', file))

    elif f_ext in EXT_Graphics:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Graphics', file))
            
    elif f_ext in EXT_CODING:
        for file in f_list:
            os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Coding', file)) 

    else:
        continue




