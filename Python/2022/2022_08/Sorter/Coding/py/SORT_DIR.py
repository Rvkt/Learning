import os
import collections

path = input('Enter Path:\n\t')
# C:\Users\Dabba\Desktop\GUI\test

EXT_DOCS = ['doc', 'docx', 'docm', 'obt', 'txt', 'csv', 'xls', 'xlsx', 'xlsm', 'pdf', 'ppt', 'pptx','pptm', 'mobi', 'epub', 'cbr']

EXT_FONT = ['ttf', 'otf']

EXT_WEB = ['html', 'css', 'scss', 'js']

EXT_AUDIO = ['wav', 'flac', 'aac', 'ogg']

EXT_VIDEO = ['3gp', 'avi', 'flv', 'mp4', 'mkv', 'mpeg']

EXT_IMAGES = ['jpeg', 'jpg', 'png', 'gif']

EXT_MUSIC = ['mp3']

EXT_ARCHIVE = ['7z', 'zip', 'rar', 'iso']

EXT_INSTALLER = ['apk', 'exe']

EXT_Illustrator = ['ai', 'svg', 'eps', 'aia']

EXT_Photoshop = ['abr', 'atn', 'psd']

EXT_SketchUp = ['skp', 'skb','IFC', 'STL', 'DAE', '3DS', 'DWG', 'DXF']

EXT_DEV = ['py']

os.chdir(path)
# print(os.getcwd())
srcpath = os.getcwd()

dstn_dirs = ['Archives', 'Audio', 'Courses', 'DevFiles', 'Documents', 'Export', 'Figma' 'Fonts', 'Form', 'Illutrator', 'Images', 'Music', 'Other', 'Phone Backup', 'Photoshop', 'Projects', 'Python', 'Raw Data', 'SketchUp', 'Software', 'Study', 'Video', 'WebFiles']

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



    # print(f_ext)
    # print(f_list)
    try:
        for f_ext, f_list in file_mapping.items():
            if f_ext in EXT_ARCHIVE:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Archives', file))
                    print(f'Files are moved {file}')
            

            elif f_ext in EXT_AUDIO:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Audio', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_DEV:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'DevFiles', file))
                    print(f'Files are moved {file}')

            
            elif f_ext in EXT_DOCS:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Documents', file))
                    print(f'Files are moved {file}')

            
            elif f_ext in EXT_FONT:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Fonts', file))
                    print(f'Files are moved {file}')

            elif f_ext in EXT_Illustrator:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Illustrator', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_IMAGES:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Images', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_MUSIC:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Music', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_Photoshop:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Photoshop', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_ARCHIVE:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Archives', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_SketchUp:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'SketchUp', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_INSTALLER:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Software', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_VIDEO:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'Video', file))
                    print(f'Files are moved {file}')


            elif f_ext in EXT_WEB:
                for file in f_list:
                    os.rename(os.path.join(srcpath, file), os.path.join(srcpath, 'WebFiles', file))
                    print(f'Files are moved {file}')


            else:
                continue


    except:
        pass