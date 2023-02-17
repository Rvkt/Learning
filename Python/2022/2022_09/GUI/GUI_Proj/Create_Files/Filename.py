import os
import itertools

# dstn = input('Destination Path:\n')
# os.chdir(dstn)


dict = {
    'DOCUMENT' : ['doc', 'docx', 'docm', 'obt', 'txt', 'csv', 'xls', 'xlsx', 'xlsm', 'pdf', 'ppt', 'pptx','pptm'],
    'EBOOK' : ['mobi', 'epub', 'cbr'],
    'FONT' : ['ttf', 'otf', 'fnt'],
    'WEB' : ['scss', 'css', 'js', 'jss', 'rjs', 'html', 'rhtml', 'php'],
    'AUDIO' : ['wav', 'flac', 'mid', 'aac', 'ogg', 'mp3'],
    'VIDEO' : ['3gp','avi', 'flv', 'mov', 'mp4', 'mkv', 'mpeg', 'srt'],
    'IMAGES' : ['bmp', 'gif', 'jpeg', 'jpg', 'png', 'tiff', 'webp'],
    'CAMERA_RAW' : ['NRW', 'NEF', 'NKSC', 'CR2', 'CRW', 'CR3', 'SR2', 'SRF', 'ARW', 'RAF', '3FR', 'FFF', 'ORF', 'GPR', 'RWL'],
    'ARCHIVE' : ['7z', 'zip', 'rar', 'iso', 'sitx', 'gz'],
    'INSTALLER' : ['apk', 'app', 'exe', 'ipa', 'jar', 'app'],
    'ILLUSTRATOR' : ['ai', 'svg', 'eps', 'aia'],
    'PHOTOSHOP' : ['abr', 'atn', 'psd'],
    'SKETCHUP' : ['skp', 'skb','IFC', 'STL', 'DAE', '3DS', 'DWG', 'DXF'],
    'DEV' : ['html'],
}

filename = []

for key in dict.keys():
    iter_dict = iter(dict.get(key))
    for ext in range(len(dict.get(key))):
        ext = next(iter_dict)
        print(f'{key}.{ext.lower()}')
        filename.append(f'{key}.{ext.lower()}')

print(len(filename))
        # Create Files
        # with open(f'{key}.{ext.lower()}', 'w'):
        #         print(f'{key}.{ext.lower()} is Created.')
        #         pass