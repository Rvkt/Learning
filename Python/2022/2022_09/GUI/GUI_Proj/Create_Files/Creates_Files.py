import os

dstn = input('Destination Path:\n')
os.chdir(dstn)

dict = {
    'DOCUMENT' : ['doc', 'docx', 'docm', 'obt', 'txt', 'csv', 'xls', 'xlsx', 'xlsm', 'pdf', 'ppt', 'pptx','pptm'],
    'EBOOK' : ['mobi', 'epub', 'cbr'],
    'FONT' : ['ttf', 'otf', 'fnt'],
    'WEB' : ['html', 'css', 'scss', 'js'],
    'AUDIO' : ['wav', 'flac', 'aac', 'ogg', 'mp3'],
    'VIDEO' : ['3gp', 'avi', 'flv', 'mp4', 'mkv', 'mpeg'],
    'IMAGES' : ['jpeg', 'jpg', 'png', 'gif'],
    'ARCHIVE' : ['7z', 'zip', 'rar', 'iso', 'sitx', 'gz'],
    'INSTALLER' : ['apk', 'app', 'exe', 'ipa', 'jar'],
    'ILLUSTRATOR' : ['ai', 'svg', 'eps', 'aia'],
    'PHOTOSHOP' : ['abr', 'atn', 'psd'],
    'SKETCHUP' : ['skp', 'skb','IFC', 'STL', 'DAE', '3DS', 'DWG', 'DXF'],
    'DEV' : ['index.html'],
}

def str_create():
    for key in dict.keys():
        i = len(dict.get(key))
        for value in (dict.get(key)):
            print(f'{key.upper()}_{str(i).zfill(2)}.{value}')
            i -= 1



'''def int_create():
    for key in dict.keys():
        i = len(dict.get(key))
        for value in (dict.get(key)):
            print(f'{str(i).zfill(2)}_{key}.{value}')
            with open(f'{str(i).zfill(2)}_{key}.{value}', 'w'):
                print(f'{str(i).zfill(2)}_{key}.{value} Created.')
                i -= 1
                pass'''


def audio():
    i = len(dict.get('AUDIO'))
    for ext in (dict.get('AUDIO')):
        '''print(f'{str(i).zfill(2)}_AUDIO.{ext}')'''
        '''print(f'AUDIO_{str(i).zfill(2)}.{ext}')'''
        with open(f'AUDIO_{str(i).zfill(2)}.{ext}', 'w'):
                print(f'AUDIO_{str(i).zfill(2)}.{ext} Created.')
                i -= 1
                pass
audio()

    