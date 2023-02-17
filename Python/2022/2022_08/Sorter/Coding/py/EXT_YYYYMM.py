import os
from datetime import date


'''
EXT_DOCS = ['doc', 'docx', 'docm', 'obt', 'txt', 'xlsx', 'xls', 'xlsm', 'csv', 'pdf', 'ppt', 'pptx', 'pptm']

EXT_EBook = ['mobi', 'epub', 'azw', 'cbr']

EXT_FONT = ['ttf', 'otf']

EXT_WEB = ['scss', 'css', 'js', 'jss', 'rjs', 'html', 'rhtml', 'psp']

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
'''




path = 'C:\\Users\\Dabba\\Desktop\\Sorter\\TEST2'
os.chdir(path)
files = os.listdir(path)



today = date.today()
year = today.strftime('%Y')
month = today.strftime('%m').zfill(2)
day = today.strftime('%d').zfill(2)

dt_path= f'{year}{month}'


ext = set()

for file in files:
    if file != '.':
        name, file_ext = os.path.splitext(file)
        file_ext = file_ext[1:]
        if file_ext != '':
            ext.add(file_ext)


for subfolder in ext:
    if not os.path.exists(subfolder):
        os.makedirs(subfolder + '/' + dt_path)

    else:
        print(f'Subfolder of {ext} Already Exists.')


print('Done!!')