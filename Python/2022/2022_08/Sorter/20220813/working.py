import os
import collections


path = input('Enter Path: ')
# C:\Users\Dabba\Desktop\GUI\test

EXT_DOCS = ['doc', 'docx', 'docm', 'obt', 'txt', 'xlsx', 'xls', 'xlsm', 'csv', 'pdf', 'ppt', 'pptx', 'pptm']

EXT_EBook = ['mobi', 'epub', 'azw', 'cbr']

EXT_FONT = ['ttf', 'otf']

EXT_WEB = ['scss', 'css', 'js', 'jss', 'rjs', 'html', 'rhtml', 'php']

EXT_AUDIO = ['flac', 'mid', 'wav', 'aac', 'ogg']

EXT_MUSIC = ['mp3']

EXT_VIDEO = ['3gp','avi', 'flv', 'mov', 'mp4', 'mkv', 'mpeg', 'srt']

EXT_IMAGES = ['bmp', 'gif', 'jpeg', 'jpg', 'png', 'tiff', 'webp']

EXT_CAMERA_RAW = ['NRW', 'NEF', 'NKSC', 'CR2', 'CRW', 'CR3', 'SR2', 'SRF', 'ARW', 'RAF', '3FR', 'FFF', 'ORF', 'GPR', 'RWL']

EXT_ARCHIVE = ['7z', 'zip', 'rar', 'iso']

EXT_INSTALLER = ['APK', 'CMD', 'IPA', 'EXE', 'BAT', 'APP', 'COM', 'COMMAND']

EXT_Illustrator = ['ai', 'aia', 'ase', 'eps', 'svg', '8bi', 'aip']

EXT_Photoshop = ['PSD', 'ABR', 'ATN', 'PLUGIN']

EXT_SketchUp = ['skp', 'skb','IFC', 'STL', 'DAE', '3DS', 'DWG', 'DXF']

EXT_PYTHON = ['py']

# EXT_ICON = ['cur', 'ico']

os.chdir(path)
# print(os.getcwd())
srcpath = os.getcwd()

dstn_dirs = ['Archives', 'Audio', 'Courses', 'DevFiles', 'Documents', 'Export',
'Figma', 'Finance', 'Fonts', 'Form', 'Illutrator', 'Images', 'Music', 'Other',
 'Phone Backup', 'Photoshop', 'Projects', 'Python', 'Raw Data', 'SketchUp', 
'Software', 'Study', 'Video', 'WebFiles']


for d in dstn_dirs:
    dir_path = os.path.join(srcpath, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    else:
        continue

# print(f'{d} Already Exists!!')


file_mapping = collections.defaultdict(list)
f_list = os.listdir(srcpath)

for f_name in f_list:
    if f_name[0] != '.':
        f_ext = f_name.split('.')[-1]
        file_mapping[f_ext].append(f_name)


for f_ext, f_list in file_mapping.items():
    # print(f_ext)
    # print(f_list)
    try:
        if f_ext in EXT_ARCHIVE:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Archives', file))

    
        elif f_ext in EXT_AUDIO:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Audio', file))


        elif f_ext in EXT_DOCS:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))

        elif f_ext in EXT_EBook:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))


        elif f_ext in EXT_FONT:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Fonts', file))

 
        elif f_ext in EXT_Illustrator:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Illutrator', file))


        elif f_ext in EXT_IMAGES:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Images', file))


        elif f_ext in EXT_MUSIC:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Music', file))


        elif f_ext in EXT_Photoshop:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Photoshop', file))


        elif f_ext in EXT_SketchUp:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'SketchUp', file))


        elif f_ext in EXT_INSTALLER:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Software', file))


        elif f_ext in EXT_VIDEO:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Video', file))


        elif f_ext in EXT_WEB:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'WebFiles', file))

        else:
            for file in f_list:
                os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Other', file))

    except:
        pass




